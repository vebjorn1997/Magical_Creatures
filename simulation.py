import json

def logistics_equation(growth_rate: float, pop_at_time: float) -> float:
    return growth_rate * pop_at_time * (1 - pop_at_time)


def calculate_population(
    growt_rate: float, pop_at_time: float, num_generations: int
) -> dict[int, float]:
    generational_population_data = {0: f"{pop_at_time:.3f}"}
    population = pop_at_time

    for generation in range(num_generations):
        population = logistics_equation(growt_rate, population)
        generational_population_data[generation + 1] = f"{population:.3f}"

    return generational_population_data


def get_validated_user_input(
    input_type: float | int,
    message: str,
    lower_bound: int = 0,
    upper_bound: int = float("inf"),
) -> float | int:
    while True:
        try:
            value = input_type(input(message))
            if value < lower_bound or value > upper_bound:
                raise ValueError(
                    f"Value must be between {lower_bound} and {upper_bound}"
                )
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def main():
    population = get_validated_user_input(float, "Enter the initial population: ", 0, 1)
    growth_rate = get_validated_user_input(float, "Enter the growth rate: ", 0, 4)
    num_generations = get_validated_user_input(int, "Enter the number of generations: ")
    output_file = input("Enter the name of the output file: ")

    population_data = calculate_population(growth_rate, population, num_generations)
    with open(f"{output_file}.json", "w", encoding="utf-8") as file:
        json.dump(population_data, file, indent=4)

    for key, value in population_data.items():
        print(f"Generation {key}: {value}")


if __name__ == "__main__":
    main()
