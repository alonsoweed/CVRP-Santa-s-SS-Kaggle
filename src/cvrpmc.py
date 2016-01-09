#! /usr/bin/python

import tsplib
import cvrp
import time
import argparse
    
def main(args):
    
    problem = tsplib.read_problem(args.infile)
    solution = cvrp.montecarlo_simulation(problem, args.ncpus,args.nprobes, args.servers)
    tsplib.write_solution(solution, filename = args.outfile)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calcula una aproximacino de la solucion optima al problema CRP mediante metodos de Monte Carlo en base a la heuristica de Clarke & Wright Savings')
    parser.add_argument("infile",
            help="El archivo tiene un problema en la especificacion de formato tsplib .vrp")
    parser.add_argument("-o", metavar="<archivo>", dest="archivo_de_salida",
            help="Coloca la salida en <archivo>")
    parser.add_argument("-j --jobs", metavar="N", dest="ncpus", type=int, 
            help="La carga se repartira entre N procesos. Por defecto es el numero de cores disponibles en el computador")
    parser.add_argument("-p --probes", metavar="N", dest="nprobes", type=int, default=100,
            help="Numero de pruebas utilizadas en cada paso del calculo")
    parser.add_argument("-s --servers", metavar="S", dest="servers", nargs="+", default = [],
            help="Direccinoes IP de los servidores adicionales usados para el calculo (experimental)")

    args = parser.parse_args()

    start_time = time.time()
    main(args)
    print "\nTiempo total: ", time.time() - start_time, " segundos"
