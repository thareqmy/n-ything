from algorithm import hill_climbing, annealing, genetic
from nything import generate_random_solution

OPTION_HILL_CLIMBING = 1
OPTION_SIMULATED_ANNEALING = 2
OPTION_GENETIC_ALGORITHM = 3

def __do_hill_climbing(chess_pieces):
    max_iteration = int(input("Max iterations: "))
    result = hill_climbing(chess_pieces, max_iteration)
    return result

def __do_simulated_annealing(chess_pieces):
    max_iteration = int(input("Max iterations: "))
    initial_temperature = int(input("Initial temperature: "))
    descent_rate = int(input("Descent rate: "))
    iteration_per_change = int(input("Iteration descent rate: "))
    result = annealing(chess_pieces, max_iteration, initial_temperature, descent_rate, iteration_per_change)
    return result

def __do_genetic_algorithm(chess_pieces):
    state_generation = int(input("Initial state generation: "))
    # result = genetic(chess_pieces, generate_random_solution, state_generation)
    # return result

def show_landing_screen():
  print(
    '''
                                                             
                                                              ███╗   ██╗              ██╗   ██╗    ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗
                                                              ████╗  ██║              ╚██╗ ██╔╝    ╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝
                                                              ██╔██╗ ██║    █████╗     ╚████╔╝        ██║   ███████║██║██╔██╗ ██║██║  ███╗
                                                              ██║╚██╗██║    ╚════╝      ╚██╔╝         ██║   ██╔══██║██║██║╚██╗██║██║   ██║
                                                              ██║ ╚████║                 ██║          ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
                                                              ╚═╝  ╚═══╝                 ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
    
    '''
  )

def show_file_prompt():
  print("Enter filepath: ", end='')
  filename = input()
  return filename

def show_option_prompt():
  option = 0
  while (option < 1 or option > 3):
    print("Press 1 to use Hill Climbing Algorithm")
    print("Press 2 to use Simulated Annealing Algorithm")
    print("Press 3 to use Genetic Algorithm")
    option = int(input())

  return option

def choose_algorithm(option, chess_pieces):
  chess_pieces = generate_random_solution(chess_pieces)
  result = chess_pieces
  if option == OPTION_HILL_CLIMBING:
    pass
    result =  __do_hill_climbing(chess_pieces)
  elif option == OPTION_SIMULATED_ANNEALING:
    pass
    result =  __do_simulated_annealing(chess_pieces)
  elif option == OPTION_GENETIC_ALGORITHM:
    pass
    # result =  __do_genetic_algorithm(chess_pieces)
  return result