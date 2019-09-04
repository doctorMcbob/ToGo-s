#togo.py 
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json
from jinja2 import Template

mainTemplate = Template(r"""<HTML><body><h1> - Show me what you got - </h1><form><ul>{% for item in combos %}<li> <input type='checkbox' name="item" value="{{ item }}"> {{ item }} </option> </li>{% endfor %}</ul><input type='submit' value="Submit"></form></body>""")
responseTemplate = Template(r"""<HTML><body><h1> You can make... </h1><ul>{% for match in matches %}<li> {{ match }} </li>{% endfor %}</ul>""")

names = """Aloo Chole with Coconut Rice
Asparagus Black Bean with Coconut Rice
Black Bean and Corn Salad with Pepita Rice
Black Bean and Corn Salad with Texas Quinoa Tabouli
Blueberry Poblano Chicken with Black Bean and Corn Salad
Blueberry Poblano Chicken with Chipotle Lime Yams
Buffalo Tofu with Black Bean and Corn Salad
Buffalo Tofu with Chipotle Lime Yams
Buffalo Tofu with Texas Quinoa Tabouli
Butter Chicken with Coconut Rice
Chicken Salad Piccata with Italian Broccoli
Chicken Salad Piccata with Lemon Capellini
Chicken Salad Piccata with Zucchini Noodle Pesto
Chicken Taquitos with Black Bean and Corn Salad
Chicken Taquitos with Guacamole
Chicken Taquitos with Salsa Rojo
Chicken Verz Cruz with Texas Quinoa Tabouli
Chipotle Lime Yams with Black Bean and Corn Salad
Chipotle Lime Yams with Coconut Rice
Chipotle Lime Yams with Pepita Rice
Chipotle Lime Yams with Texas Quinoa Tabouli
Chipotle Salmon Cake with Indonesian Rice
Chipotle Salmon Cake with Roasted Potato Dill Salad
Chipotle Salmon Cake with Zucchini Noodle Pesto
Coconut Mango Chicken with Coconut Rice
Coconut Mango Chicken with Indonesian Rice
Coconut Mango Chicken with Roasted Vegetables
Coconut Mango Chicken with Sweet Chili Vegetables
Cuban Chicken Thighs with Chipotle Lime Yams
Cuban Picadillo with Black Bean and Corn Salad
Cuban Picadillo with Chipotle Lime Yams
Cuban Picadillo with Coconut Rice
Cuban Picadillo with Pepita Rice
Cuban Picadillo with Seasoned Basmati Rice
Curried Cashew Tofu with Coconut Rice
Curried Cashew Tofu with Ginger Udon
Curried Cashew Tofu with Sesame Edamame Quinoa
East of the Lake Tofu with Asian Capellini
East of the Lake Tofu with Indonesian Rice
East of the Lake Tofu with Kelp Noodle Salad
Falafel with Lemon Tahini
Glazed Tempeh Fajitas with Black Bean and Corn Salad
Glazed Tempeh Fajitas with Pepita Rice
Glazed Tempeh Fajitas with Southwest Corn Pudding
Glazed Tempeh Fajitas with Spanish Rice
Grilled Chicken Vera Cruz with Black Bean and Corn Salad
Grilled Chicken Vera Cruz with Pepita Rice
Grilled Chicken Vera Cruz with Southwest Corn Pudding
Grilled Chicken Vera Cruz with Texas Quinoa Tabouli
Grilled Chicken with Asian Capellini
Grilled Chicken with Asparagus
Grilled Chicken with Asparagus and Orzo Salad
Grilled Chicken with Asparagus in Black Bean Sauce
Grilled Chicken with Autumn Orzo
Grilled Chicken with Bacon Bleu Cheese Potato Salad
Grilled Chicken with Black Bean and Corn Salad
Grilled Chicken with California Potato Salad
Grilled Chicken with Cauliflower Tahini
Grilled Chicken with Chipotle Lime Yams
Grilled Chicken with Chorizo Apple Cornbread Dressing
Grilled Chicken with Emerald City Salad
Grilled Chicken with Garlic Parmesan Mashed Potatoes
Grilled Chicken with Ginger Udon
Grilled Chicken with Gremolata Green Beans
Grilled Chicken with Grilled Green Beans
Grilled Chicken with Indonesian Rice
Grilled Chicken with Italian Broccoli
Grilled Chicken with Lemon Capellini
Grilled Chicken with Maple Cranberry Wild Rice
Grilled Chicken with Moroccan Asparagus Potato Salad
Grilled Chicken with Moroccan Yams
Grilled Chicken with Mushroom Risotto Cake
Grilled Chicken with Pecorino Quinoa and Kale
Grilled Chicken with Pesto Tortellini
Grilled Chicken with Pumpkin Ravioli
Grilled Chicken with Red Curry Vegetables
Grilled Chicken with Roasted Brussels Sprouts
Grilled Chicken with Roasted Fingerling Potatoes
Grilled Chicken with Roasted Mushroom Risotto
Grilled Chicken with Roasted Squash w/Apples and Bacon
Grilled Chicken with Roasted Tomato Pasta
Grilled Chicken with Roasted Vegetables
Grilled Chicken with Roasted Winter Vegetables
Grilled Chicken with Roasted Yam and Kale Salad
Grilled Chicken with Sage Stuffing
Grilled Chicken with Sicilian Orzo
Grilled Chicken with Smoked Mozzarella Pasta
Grilled Chicken with Sweet Chili Vegetables
Grilled Chicken with Texas Quinoa Tabouli
Grilled Chicken with Thai Glazed Bok Choy
Grilled Chicken with Zucchini Noodle Pesto
Herbed Chicken Thigh with Lemon Capellini
Indonesian Rice with Sesame Snap Peas
Kelp Noodles with Sesame Snap Peas
Lemon Capellini with Italian Broccoli
Lemon Capellini with Zucchini Noodle Pesto
Lemon Dill Cod with Emerald City Salad
Lemon Dill Cod with Italian Broccoli
Lemon Dill Cod with Roasted Fingerling Potatoes
Mango Curry Tofu with Brown Rice
Mango Curry Tofu with Coconut Rice
Mango Curry Tofu with Indonesian Rice
Mango Curry Tofu with Kelp Noodles
Momo's chicken with Coconut Rice
Moroccan Chicken with Chipotle Lime Yams
Moroccan Chicken with Roasted Fingerling Potatoes
Moroccan Chicken with Yams
Orange Sesame Short Ribs with Asian Capellini
Orange Sesame Short Ribs with Coconut Rice
Orange Sesame Short Ribs with Sicilian Orzo
Oven Roasted Chicken with Black Bean and Corn Salad
Oven Roasted Chicken with Chipotle Lime Yams
Oven Roasted Chicken with Italian Broccoli
Oven Roasted Chicken with Roasted Vegetables
Oven Roasted Chicken with Smoked Mozzarella Pasta
Oven Roasted Chicken with Texas Quinoa Tabouli
Pan Fried Tofu w/Mushrooms with Coconut Rice
Parmesan Chicken Fingers with Black Bean and Corn Salad
Parmesan Chicken Fingers with Italian Broccoli
Parmesan Chicken Fingers with Lemon Capellini
Parmesan Chicken Fingers with Marinara
Parmesan Chicken Fingers with Pesto Tortellini
Parmesan Chicken Fingers with Roasted Cauliflower w Tahini
Parmesan Chicken Fingers with Roasted Tomato Pasta
Parmesan Chicken Fingers with Sicilian Orzo
Parmesan Chicken Fingers with Zucchini Noodle Pesto
Pepper Beef with Asian Capellini
Pepper Beef with Asparagus
Pepper Beef with Asparagus and Orzo Salad
Pepper Beef with Asparagus in Black Bean Sauce
Pepper Beef with Black Bean and Corn Salad
Pepper Beef with California Potato Salad
Pepper Beef with Cauliflower Tahini
Pepper Beef with Chipotle Lime Yams
Pepper Beef with Emerald City Salad
Pepper Beef with Garlic Parmesan Mashed Potatoes
Pepper Beef with Gremolata Green Beans
Pepper Beef with Italian Broccoli
Pepper Beef with Lemon Capellini
Pepper Beef with Mushroom Risotto Cake
Pepper Beef with Pesto Tortellini
Pepper Beef with Roasted Brussels Sprouts
Pepper Beef with Roasted Fingerling Potatoes
Pepper Beef with Roasted Squash w/Apples and Bacon
Pepper Beef with Roasted Vegetables
Pepper Beef with Roasted Winter Vegetables
Pepper Beef with Smoked Mozzarella Pasta
Pepper Beef with Walnut Beets
Pepper Beef with Zucchini Noodle Pesto
Pesto Tortellini with Italian Broccoli
Pesto Tortellini with Zucchini Noodle Pesto
Polenta with Black Beans and Tomatoes
Red Curry Cod with Asian Capellini
Red Curry Cod with Kelp Noodle Salad
Red Curry Cod with Smoked Mozzarella Pasta
Red Curry Vegetables with Asian Capellini
Red Curry Vegetables with Coconut Rice
Roasted Tomato Pasta with Italian Broccoli
Roasted Tomato Pasta with Zucchini Noodle Pesto
Salmon with Asparagus
Salmon with Asparagus and Orzo Salad
Salmon with Asparagus in Black Bean Sauce
Salmon with Autumn Orzo
Salmon with Black Bean and Corn Salad
Salmon with Cauliflower Tahini
Salmon with Chipotle Lime Yams
Salmon with Emerald City Salad
Salmon with Gremolata Green Beans
Salmon with Indonesian Rice
Salmon with Italian Broccoli
Salmon with Lemon Capellini
Salmon with Moroccan Asparagus Potato Salad
Salmon with Moroccan Yams
Salmon with Pecorino Quinoa and Kale
Salmon with Pumpkin Ravioli
Salmon with Red Curry Asparagus Rice
Salmon with Red Curry Vegetables
Salmon with Roasted Brussels Sprouts
Salmon with Roasted Fingerling Potatoes
Salmon with Roasted Potato Dill Salad
Salmon with Roasted Squash w/Apples and Bacon
Salmon with Roasted Tomato Pasta
Salmon with Roasted Vegetables
Salmon with Roasted Winter Vegetables
Salmon with Roasted Yams and Kale
Salmon with Sesame Quinoa Edamame Salad
Salmon with Sweet Chili Vegetables
Salmon with Tangerine Wild RIce and Farro
Salmon with Thai Bok Choy
Salmon with Zucchini Noodle Pesto
Sicilian Orzo with Italian Broccoli
Southeast Asian Tempeh with Asian Capellini
Southeast Asian Tempeh with Brown Rice
Southeast Asian Tempeh with Coconut Rice
Southeast Asian Tempeh with Indonesian Rice
Southeast Asian Tempeh with Kelp Noodles
Southeast Asian Tempeh with Red Curry Vegetables
Southeast Asian Tempeh with Sweet Chili Vegetables
Southeast Asian Tempeh with Thai Glazed Bok Choy
Southwest Corn Pudding with Black Bean and Corn Salad
Spicy Chicken Thighs with Asian Capellini
Spicy Chicken Thighs with Black Bean and Corn Salad
Spicy Chicken Thighs with Black Beans and Rice
Spicy Chicken Thighs with California Potato Salad
Spicy Chicken Thighs with Cauliflower Tahini
Spicy Chicken Thighs with Chipotle Lime Yams
Spicy Chicken Thighs with Emerald City Salad
Spicy Chicken Thighs with Gremolata Green Beans
Spicy Chicken Thighs with Moroccan Yams
Spicy Chicken Thighs with Red Curry Vegetables
Spicy Chicken Thighs with Roasted Brussels Sprouts
Spicy Chicken Thighs with Roasted Fingerling Potatoes
Spicy Chicken Thighs with Roasted Squash w/Apples and Bacon
Spicy Chicken Thighs with Roasted Vegetables
Spicy Chicken Thighs with Roasted Winter Vegetables
Spicy Chicken Thighs with Smoked Mozzarella Pasta
Spicy Chicken Thighs with Sweet Chili Vegetables
Spicy Chicken Thighs with Texas Quinoa Tabouli
Spicy Chicken Thighs with Thai Glazed Bok Choy
Spicy Tofu with Brown Rice
Steph's Tofu with Asian Capellini
Steph's Tofu with Asparagus
Steph's Tofu with Asparagus in Black Bean Sauce
Steph's Tofu with Black Bean and Corn Salad
Steph's Tofu with Brown Rice
Steph's Tofu with Chipotle Lime Yams
Steph's Tofu with Coconut Mashed Yams
Steph's Tofu with Coconut Rice
Steph's Tofu with Emerald City Salad
Steph's Tofu with Ginger Udon
Steph's Tofu with Gremolata Green Beans
Steph's Tofu with Indonesian Rice
Steph's Tofu with Italian Broccoli
Steph's Tofu with Kelp Noodle Salad
Steph's Tofu with Moroccan Yams
Steph's Tofu with Red Curry Asparagus Rice
Steph's Tofu with Red Curry Vegetables
Steph's Tofu with Roasted Brussels Sprouts
Steph's Tofu with Roasted Vegetables
Steph's Tofu with Sesame Quinoa Edamame Salad
Steph's Tofu with Sweet Chili Vegetables
Steph's Tofu with Tahini Cauliflower
Steph's Tofu with Texas Quinoa Tabouli
Steph's Tofu with Thai Glazed Bok Choy
Steph's Tofu with Turkish Garbanzo Salad
Steph's Tofu with Zucchini Noodle Pesto
Sweet Chili Vegetables with Asian Capellini
Sweet Chili Vegetables with Coconut Rice
Tandoori Tofu with Asian Capellini
Tandoori Tofu with Brown Rice
Tandoori Tofu with Grilled Green Beans
Tandoori Tofu with Indonesian Rice
Thai Chili Tofu with Asian Capellini
Thai Chili Tofu with Coconut Rice
Thai Chili Tofu with Glazed Bok Choy
Thai Chili Tofu with Indonesian Rice
Thai Chili Tofu with Kelp Noodles
Thai Chili Tofu with Red Curry Vegetables
Thai Chili Tofu with Sweet Chili Vegetables
Thai Glazed Bok Choy with Asian Capellini
Thai Glazed Bok Choy with Coconut Rice
Thai Salmon with Asian Capellini
Thai Salmon with Coconut Rice
Thai Salmon with Indonesian Rice
Thai Salmon with Kelp Noodles
Thai Salmon with Sesame Snap Peas
Thai Steak Salad with Asian Capellini
Thai Steak Salad with Asparagus Black Bean
Thai Steak Salad with Chipotle Lime Yams
Thai Steak Salad with Coconut Rice
Thai Steak Salad with Ginger Udon
Thai Steak Salad with Glazed Bok Choy
Thai Steak Salad with Grilled Green Beans
Thai Steak Salad with Indonesian Rice
Thai Steak Salad with Kelp Noodles
Thai Steak Salad with Lemon Capellini
Thai Steak Salad with Red Curry Vegetables
Thai Steak Salad with Sesame Edamame Quinoa
Thai Steak Salad with Sesame Snap Peas
Thai Steak Salad with Sweet Chili Vegetables
Thai Steak with Red Curry Asparagus Rice
Turkey Loaf with Mashed Yams and Goat Cheese
Turkey Meatloaf with Autumn Orzo
Turkey Meatloaf with Bacon Bleu Cheese Potato Salad
Turkey Meatloaf with Black Bean and Corn Salad
Turkey Meatloaf with California Potato Salad
Turkey Meatloaf with Chipotle Lime Yams
Turkey Meatloaf with Emerald City Salad
Turkey Meatloaf with Garlic Parmesan Mashed Potatoes
Turkey Meatloaf with Italian Broccoli
Turkey Meatloaf with Lemon Capellini
Turkey Meatloaf with Mushroom Risotto Cake
Turkey Meatloaf with Pecorino Quinoa and Kale
Turkey Meatloaf with Pesto Tortellini
Turkey Meatloaf with Roasted Fingerling Potatoes
Turkey Meatloaf with Roasted Tomato Pasta
Turkey Meatloaf with Roasted Vegetables
Turkey Meatloaf with Roasted Yam and Kale
Turkey Meatloaf with Sicilian Orzo
Turkey Meatloaf with Smoked Mozzarella Pasta
Turkey Meatloaf with Texas Quinoa Tabouli
Turkey Meatloaf with Walnut Beets
Turkey Meatloaf with Zucchini Noodle Pesto
Turkey with Gremolata Green Beans
Turkey with Maple Cranberry Wild Rice
Turkey with Mashed Potatoes and Turkey Gravy
Turkey with Mashed Potatoes, Green Beans and Turkey G
Turkey with Mashed Yams and Goat Cheese
Turkey with Roasted Brussels Sprouts
Turkey with Sage Stuffing""".splitlines()

COMBOS = {}

for togo in names:
    item1, item2 = togo.split(" with ")
    if item1 not in COMBOS: COMBOS[item1] = []
    if item2 not in COMBOS[item1]: COMBOS[item1].append(item2)
    if item2 not in COMBOS: COMBOS[item2] = []
    if item1 not in COMBOS[item2]: COMBOS[item2].append(item1)

def parse(items):
    matches = []
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                for name in names:
                    if item1 in name and item2 in name:
                        matches.append(name)
    return matches

def main(request):
    if 'item' in request.params:
        items = request.params.dict_of_lists()['item']
        matches = parse(items)
        return Response(responseTemplate.render(matches=matches))
    else:
        return Response(mainTemplate.render(combos=list(COMBOS.keys())))

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()