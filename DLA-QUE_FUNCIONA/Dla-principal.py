import lichtenberg as lb
from lichtenberg.archive import save
from pathlib import Path
from random import randint


def main():
    width = 300
    height = 300

    lb.set_random_seed(randint(0, 32768))
    
    def loop(current_loop, max_loop, cells):
        if current_loop % 100 == 0:
            print(f'loop:{current_loop}/{max_loop}')
        return False

    # Inicializar un modelo de ruptura
    num_particle = 15000
    model = lb.DLABreakModel(width, height, num_particle=num_particle)

    # Simulacion
    sim = lb.Simulator(width, height, model)
    sim.breakdown(width // 2, height // 2)
    sim.simulate(max_loop=40000, callback_on_loop=loop)#max_loop es la cantidad de iteraciones

    # salida
    save(sim.cells, Path(__file__).stem, output_binary=True, output_mono=True, output_gray=True)


if __name__ == '__main__':  
    main()
