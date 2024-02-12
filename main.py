from annealing import Annealer
import salesman
import pygame


SIZE = (600, 600)



if __name__ == "__main__":
    salesman.init_display(SIZE)

    start = salesman.new_problem(20)
    salesman.draw_problem(start)
    
    
    annealer = Annealer(start, salesman.route_neighbor, salesman.route_dist, lambda t: t*0.9995, start_temp = 0.1)
    for _ in annealer.loop(1000):
        salesman.draw_clear()
        
        salesman.draw_problem(annealer.best_state, (255, 220, 220))
        salesman.draw_problem(annealer.state)
        
        salesman.refresh()
        
        print(annealer.temp )

    print("done")
    while True:
        salesman.refresh()