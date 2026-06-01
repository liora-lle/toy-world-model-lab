import numpy as np
import torch
from torch.utils.data import Dataset


ACTION_TO_DELTA = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


ACTION_TO_ID = {
    "up": 0,
    "down": 1,
    "left": 2,
    "right": 3,
}

ID_TO_ACTION = {
    0: "up",
    1: "down",
    2: "left",
    3: "right",
}


def generate_ball_image(image_size=32, x=16, y=16, radius=2):
    """
    Generate a simple grayscale image with a white ball on a black background.

    Args:
        image_size: The height and width of the square image.
        x: The x-coordinate of the ball center.
        y: The y-coordinate of the ball center.
        radius: The radius of the ball.

    Returns:
        image: A numpy array with shape [image_size, image_size].
    """
    image = np.zeros((image_size, image_size), dtype=np.float32)

    for row in range(image_size):
        for col in range(image_size):
            distance = np.sqrt((col - x) ** 2 + (row - y) ** 2)

            if distance <= radius:
                image[row, col] = 1.0

    return image


def update_position(x, y, action, image_size=32, radius=2, step_size=4):
    """
    Update the ball position according to the action.

    Args:
        x: Current x-coordinate.
        y: Current y-coordinate.
        action: One of "up", "down", "left", "right".
        image_size: The height and width of the square image.
        radius: The ball radius.
        step_size: Number of pixels moved by one action.

    Returns:
        new_x, new_y: Updated position after applying the action.
    """
    if action not in ACTION_TO_DELTA:
        raise ValueError(f"Unknown action: {action}")

    dx, dy = ACTION_TO_DELTA[action]

    new_x = x + dx * step_size
    new_y = y + dy * step_size

    min_pos = radius
    max_pos = image_size - radius - 1

    new_x = max(min_pos, min(new_x, max_pos))
    new_y = max(min_pos, min(new_y, max_pos))

    return new_x, new_y


def generate_episode(
    image_size=32,
    sequence_length=6,
    radius=2,
    start_x=16,
    start_y=16,
    step_size=4,
):
    """
    Generate a ball movement episode.

    Args:
        image_size: The height and width of the square image.
        sequence_length: Number of frames in the episode.
        radius: The ball radius.
        start_x: Initial x-coordinate.
        start_y: Initial y-coordinate.
        step_size: Number of pixels moved by one action.

    Returns:
        frames: A list of images.
        actions: A list of actions between frames.
        positions: A list of ball positions.
    """
    possible_actions = list(ACTION_TO_DELTA.keys())

    x, y = start_x, start_y

    frames = []
    positions = []
    episode_actions = []

    for step in range(sequence_length):
        image = generate_ball_image(
            image_size=image_size,
            x=x,
            y=y,
            radius=radius,
        )

        frames.append(image)
        positions.append((x, y))

        if step < sequence_length - 1:
            action = np.random.choice(possible_actions)
            episode_actions.append(action)

            x, y = update_position(
                x=x,
                y=y,
                action=action,
                image_size=image_size,
                radius=radius,
                step_size=step_size,
            )

    return frames, episode_actions, positions



class BallWorldModelDataset(Dataset):
    """
    PyTorch Dataset for the toy ball world model.

    Each sample is:

        observation + action -> next_observation
    """

    def __init__(
        self,
        num_sequences=500,
        sequence_length=6,
        image_size=32,
        radius=2,
        step_size=4,
    ):
        self.samples = []

        for _ in range(num_sequences):
            frames, actions, positions = generate_episode(
                image_size=image_size,
                sequence_length=sequence_length,
                radius=radius,
                start_x=image_size // 2,
                start_y=image_size // 2,
                step_size=step_size,
            )

            for i, action in enumerate(actions):
                observation = frames[i]
                next_observation = frames[i + 1]
                action_id = ACTION_TO_ID[action]

                self.samples.append(
                    {
                        "observation": observation,
                        "action": action_id,
                        "next_observation": next_observation,
                    }
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        sample = self.samples[index]

        observation = torch.tensor(sample["observation"], dtype=torch.float32).unsqueeze(0)
        action = torch.tensor(sample["action"], dtype=torch.long)
        next_observation = torch.tensor(sample["next_observation"], dtype=torch.float32).unsqueeze(0)

        return {
            "observation": observation,
            "action": action,
            "next_observation": next_observation,
        }