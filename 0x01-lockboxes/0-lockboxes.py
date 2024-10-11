#!/usr/bin/python3
"""Lockboxes, a module for determining if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    """
    if not boxes:
        return False

    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
