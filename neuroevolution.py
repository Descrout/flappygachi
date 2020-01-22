import numpy as np
import random


class Genetics:
    @staticmethod
    def calculate_fitness(dead_gachis):
        sum_score = 0
        for d_gachi in dead_gachis:
            sum_score += d_gachi.score * d_gachi.score
        
        for d_gachi in dead_gachis:
            d_gachi.fitness = (d_gachi.score * d_gachi.score) / sum_score
        


    @staticmethod
    def pick_one(dead_gachis):
        f_sum = 0

        for d_gachi in dead_gachis:
            f_sum += d_gachi.fitness
            print("fitness : ",d_gachi.fitness)

        r = random.random() * f_sum
        sum = 0
        for d_gachi in dead_gachis:
            if r <= (sum := sum + d_gachi.fitness):
                print("picked : ",d_gachi.fitness)
                return d_gachi
        return None        

    @staticmethod
    def mutate(gachi_arr,rate):
        def mut_func(el):
            if random.random() < rate:
                return el + random.gauss(0,0.1)
            else:
                return el

        mut_vec = np.vectorize(mut_func)
        return mut_vec(gachi_arr)

    @staticmethod
    def crossover(dead_gachis):
        mother = Genetics.pick_one(dead_gachis)
        father = Genetics.pick_one(dead_gachis)

        weights_halfs = [int(len(w.ravel())/2) for w in mother.brain.weights]
        biases_half = int(len(mother.brain.biases[0])/2)

        weights_shapes = [w.shape for w in mother.brain.weights]
        bias_shapes = [b.shape for b in mother.brain.biases]

        mother_weights = [w.flatten()[h:] for w,h in zip(mother.brain.weights,weights_halfs)]
        father_weights = [w.flatten()[:h] for w,h in zip(father.brain.weights,weights_halfs)]

        mother_biases = [b.flatten()[biases_half:] for b in mother.brain.biases]
        father_biases = [b.flatten()[:biases_half] for b in father.brain.biases]

        from gachi import Gachi
        temp_gachi = Gachi(mother.anim.img)
        temp_gachi.brain.weights = [Genetics.mutate(np.concatenate((mw,fw)).reshape(ws),0.1) for mw,fw,ws in zip(mother_weights, father_weights, weights_shapes)]
        temp_gachi.brain.biases = [Genetics.mutate(np.concatenate((mb,fb)).reshape(bs),0.1) for mb,fb,bs in zip(mother_biases,father_biases,bias_shapes)]
        return temp_gachi

    @staticmethod
    def next_generation(flappygachi):
        Genetics.calculate_fitness(flappygachi.dead_gachis)
        flappygachi.gachis = [Genetics.crossover(flappygachi.dead_gachis) for _ in range(30)]
        flappygachi.dead_gachis = []
        
        


class NeuralNetwork:
    def __init__(self, layer_sizes):
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in weight_shapes]
        self.biases = [np.random.rand(s,1) for s in layer_sizes[1:]] 
        self.learning_rate = 0.1

    def predict(self,a):
        for w,b in zip(self.weights, self.biases):
            a = np.matmul(w,a) + b
            a = np.vectorize(self.sigmoid)(a)
        return a

    @staticmethod
    def sigmoid(x):
        return 1/(1+np.exp(-x))

    @staticmethod
    def d_sigmoid(x):
        return x * (1 - x)