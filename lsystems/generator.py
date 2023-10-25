class Generator:
    from lsystems.tortoise import Tortoise

    def __init__(self, lsys, axiom, nsteps):
        self.lsys = lsys
        self.axiom = axiom
        self.nsteps = nsteps
        self.stack = []

    def generate(self):
        predecessors = self.axiom
        steps = [self.axiom]
        for _ in range(self.nsteps):
            successors = self.lsys.step(predecessors)
            predecessors = successors
            steps.append(successors)
        return steps

    def generate_tortoise(self):
<<<<<<< HEAD
        from lsystems.tortoise import Tortoise

=======
>>>>>>> dev
        predecessors = self.axiom
        steps = [self.axiom]
        tort = Tortoise()
        for _ in range(self.nsteps):
            successors = self.lsys.step(predecessors)
            predecessors = successors
            steps.append(successors)
            for successor in successors:
                if successor == "F":
                    tort.forward(draw=True)
                if successor == "-":
                    tort.rotate(-90)
                if successor == "+":
                    tort.rotate(90)
        return steps, tort.get_history()


if __name__ == "__main__":
    from lsys import Lsys
    from draw import draw_coords

    # test_lsys = Lsys(["A", "B"], {"A": "AB"})
    # test_lsys.add_rules({"B": "AA"})

    # test_generator = Generator(test_lsys, "A", 10)
    # print(test_generator.generate())
    test_lsys = Lsys(["F", "f", "+", "-"], {"F": "F-F+F+FF-F-F+F"})
    test_gen = Generator(test_lsys, "F-F-F-F", 3)
    steps, history = test_gen.generate_tortoise()
    print(steps, history)
    draw_coords(history, 200)
