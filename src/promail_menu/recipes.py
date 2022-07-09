import re
from typing import List

import requests


class Meal:
    '''A meal you can cook.'''

    def __init__(self, str_meal:str, str_category, str_instructions, str_meal_thumb, str_youtube, ingredients, **kwargs):
        """Initializes meal class"""
        self.youtube = str_youtube
        self.thumbnail = str_meal_thumb
        self.name = str_meal
        self.instructions = str_instructions
        self.category = str_category
        self.ingredients = ingredients


class Api:
    api_base_url = "https://www.themealdb.com/api/json/v1/1/"

    def form_url(self, suffix: str) -> str:
        """Form URL."""
        return f"{self.api_base_url}{suffix}"

    def query_api(self, suffix: str) -> list:
        """Query Api."""
        url = self.form_url(suffix)
        data = requests.get(url).json().get("meals", [])
        data = self.convert_to_snake_case(data)
        return self.combine_ingredients(data)

    def random(self) -> Meal:
        """Get Random Meal from API."""
        data = self.query_api("random.php")
        return Meal(**data[0])

    def combine_ingredients(self, meal_data) -> List[tuple]:
        """Adds an 'ingredients' property to each meal in meal_data.

            ingredients are in the form (ingredient, amount).
        """
        for data in meal_data:
            ingredients = []
            for i in range(1, 40):
                ingredient = data.get(f"str_ingredient{i}", '')
                if ingredient:
                    ingredients.append((ingredient, data.get(f"str_measure{i}", '')))
            data['ingredients'] = ingredients
        return meal_data

    @staticmethod
    def convert_to_snake_case(q_list: List[dict]):
        """Converts keys from camel case to snake case.
        Examples:
            >>> [{"strIngredients": "apple"}, {"strIngredients": "Orange"}]
            [{"str_ingredients": "apple"}, {"str_ingredients": "Orange"}]
        """
        formatted_list = []
        for data in q_list:
            new_dict = {}
            formatted_list.append(new_dict)
            for key, value in data.items():
                new_key = re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower()
                new_dict[new_key] = value

        return formatted_list
