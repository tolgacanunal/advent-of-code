from dataclasses import dataclass
from math import lcm
import os

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


@dataclass
class Node:
    name: str
    left: str
    right: str

    def __hash__(self):
        return hash(self.name)


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    instructions, nodes_raw = file_content.split("\n\n")

    graph = {}

    for node_raw in nodes_raw.split("\n"):
        name, instruction = node_raw.split(" = ")
        left, right = instruction[1:-1].split(", ")
        graph[name] = Node(name=name, left=left, right=right)

    return (graph, instructions)


def get_part_one_solution(data: tuple[dict[str, Node], str]) -> str:
    graph, instructions = data

    current_node = graph['AAA']
    count = 0

    while True:
        for instruction in instructions:
            count += 1
            current_node = graph[current_node.left] if instruction == 'L' else graph[current_node.right]
            if current_node.name == 'ZZZ':
                return count


def get_part_two_solution(data: tuple[dict[str, Node], str]) -> str:
    graph, instructions = data

    current_nodes = set(
        map(
            lambda key: graph[key],
            filter(lambda key: key.endswith('A'), graph.keys())
        )
    )

    step = 0
    lcm_value = 1

    while True:
        for instruction in instructions:
            step += 1

            for navigated_node in current_nodes.copy():
                current_nodes.remove(navigated_node)
                next_node = graph[navigated_node.left] if instruction == 'L' else graph[navigated_node.right]
                if next_node.name.endswith('Z'):
                    lcm_value = lcm(lcm_value, step)
                else:
                    current_nodes.add(next_node)

            if not current_nodes:
                return lcm_value


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
