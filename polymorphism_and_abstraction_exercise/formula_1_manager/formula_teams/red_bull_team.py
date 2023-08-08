from oop.polymorphism_and_abstraction_exercise.formula_1_manager.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expenses_per_race = -250_000
    sponsors_reward = {'Oracle': {1: 1_500_000,
                                  2: 800_000},
                       'Honda': {8: 20_000,
                                 10: 10_000}}

    def calculate_revenue_after_race(self, race_pos: int):
        return self.revenue_calculator(race_pos)
