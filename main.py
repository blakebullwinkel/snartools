import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial
from snartoolsmod import *

Builder.load_string('''
#: import main main
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<DiningButton>:
    font_size: 38
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.85, 0.85, 0.85, 1
<DirectionButton>:
    font_size: 20
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.85, 0.85, 0.85, 1
    size_hint: 0.25, 0.1
<SubmenuButton>:
    font_size: 28
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.7, 0.7, 0.7, 1
    size_hint_y: None
    height: '40sp'
    text_size: self.size
    halign: 'left'
    valign: 'middle'
    padding_x: 15
<ItemButton>:
    font_size: 28
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.85, 0.85, 0.85, 1
    size_hint_y: None
    height: '40sp'
    text_size: self.size
    halign: 'left'
    valign: 'middle'
    padding_x: 50
<InitialOrderButton>:
    font_size: 28
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.85, 0.85, 0.85, 1
    size_hint_y: None
    height: '40sp'
    text_size: self.size
    halign: 'left'
    valign: 'middle'
    padding_x: 50
<ToolButton>:
    font_size: 28
    color: 0.447, 0.094, 0.737, 1
    background_normal: ''
    background_color: 0.85, 0.85, 0.85, 1
    size_hint_y: None
<InstructionsLabel>:
    font_size: 24
    size_hint_y: None
    color: 0.447, 0.094, 0.737, 1
    text_size: root.width, None
    size: self.texture_size
    padding_x: 20
<SubLabel>:
    font_size: 20
    size_hint_y: None
    color: 0.45, 0.45, 0.45, 1
    text_size: root.width, None
    size: self.texture_size
    padding_x: 20
    padding_y: 3
<OrderLabel>:
    font_size: 20
    size_hint_y: None
    color: 0.447, 0.094, 0.737, 1
    text_size: root.width, None
    size: self.texture_size
    padding_x: 20
    padding_y: 5
<HomeScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 10
        Label:
            font_size: 78
            color: 0.447, 0.094, 0.737, 1
            text: "snartools"
            size_hint: 1, .8
        Label:
            font_size: 24
            color: 0.447, 0.094, 0.737, 1
            text: "Select a dining facility"
            size_hint: 1, .4
        DiningButton:
            text: "Whitman's"
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "whitmans_menu"
        DiningButton:
            text: "Lee After Dark"
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "lees_menu"
        DiningButton:
            text: "Eco Cafe"
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "ecocafe_menu"
<WhitmansMenu>:
    fryer: fryer
    grill: grill
    beverages: beverages
    vegan: vegan
    on_enter:
        root.itemList = root.initialize_list()
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "home_screen"
                root.fryer.state = 'normal'
                root.grill.state = 'normal'
                root.beverages.state = 'normal'
                root.vegan.state = 'normal'
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                root.manager.get_screen('length_exact').itemList = root.itemList
                root.manager.get_screen('length_range').itemList = root.itemList
                root.manager.get_screen('price_exact').itemList = root.itemList
                root.manager.get_screen('price_range').itemList = root.itemList
                root.manager.get_screen('more_exact').itemList = root.itemList
                root.manager.get_screen('more_exact_two').itemList = root.itemList
                root.manager.get_screen('more_range').itemList = root.itemList
                root.manager.get_screen('more_range_two').itemList = root.itemList
                root.manager.get_screen('length_exact').len_exact_input.hint_text = "Integer 1-"+str(len(root.itemList.longOrder(7)))
                root.manager.get_screen('length_range').len_range_input_upper.hint_text = "Integer less than "+str((root.itemList.longestOrder(7))+1)
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 0.93}
        padding: 0, 35
        InstructionsLabel:
            text: "Select all menus and items to EXCLUDE from your order"
        ScrollView:
            GridLayout:
                cols: 1
                padding: 20
                spacing: 5
                size_hint_y: None
                height: self.minimum_height
                SubmenuButton:
                    id: fryer
                    text: 'Fryer'
                    on_state: root.modify_state(fryer.state, 'fryer', 7)
                ItemButton:
                    id: fryer_item1
                    text: 'Fried Green Beans'
                    on_state: root.modify_list(root.itemList, fryer_item1.state, 'Fried Green Beans')
                ItemButton:
                    id: fryer_item2
                    text: 'PB&J Fries'
                    on_state: root.modify_list(root.itemList, fryer_item2.state, 'PB&J Fries')
                ItemButton:
                    id: fryer_item3
                    text: 'French Fries'
                    on_state: root.modify_list(root.itemList, fryer_item3.state, 'French Fries')
                ItemButton:
                    id: fryer_item4
                    text: 'Onion Rings'
                    on_state: root.modify_list(root.itemList, fryer_item4.state, 'Onion Rings')
                ItemButton:
                    id: fryer_item5
                    text: 'Chicken Tenders'
                    on_state: root.modify_list(root.itemList, fryer_item5.state, 'Chicken Tenders')
                ItemButton:
                    id: fryer_item6
                    text: 'Mozzarella Sticks'
                    on_state: root.modify_list(root.itemList, fryer_item6.state, 'Mozzarella Sticks')
                ItemButton:
                    id: fryer_item7
                    text: 'Grilled Honey Bun'
                    on_state: root.modify_list(root.itemList, fryer_item7.state, 'Grilled Honey Bun')
                SubmenuButton:
                    id: grill
                    text: 'Grill & Deli'
                    on_state: root.modify_state(grill.state, 'grill', 15)
                ItemButton:
                    id: grill_item1
                    text: 'Hamburger'
                    on_state: root.modify_list(root.itemList, grill_item1.state, 'Hamburger')
                ItemButton:
                    id: grill_item2
                    text: 'Cheeseburger'
                    on_state: root.modify_list(root.itemList, grill_item2.state, 'Cheeseburger')
                ItemButton:
                    id: grill_item3
                    text: 'Bacon Burger'
                    on_state: root.modify_list(root.itemList, grill_item3.state, 'Bacon Burger')
                ItemButton:
                    id: grill_item4
                    text: 'Hot Dog'
                    on_state: root.modify_list(root.itemList, grill_item4.state, 'Hot Dog')
                ItemButton:
                    id: grill_item5
                    text: 'Chicken Patty'
                    on_state: root.modify_list(root.itemList, grill_item5.state, 'Chicken Patty')
                ItemButton:
                    id: grill_item6
                    text: 'Grilled Chicken'
                    on_state: root.modify_list(root.itemList, grill_item6.state, 'Grilled Chicken')
                ItemButton:
                    id: grill_item7
                    text: 'Chicken Cordon Bleu'
                    on_state: root.modify_list(root.itemList, grill_item7.state, 'Chicken Cordon Bleu')
                ItemButton:
                    id: grill_item8
                    text: 'Shawarma Chicken'
                    on_state: root.modify_list(root.itemList, grill_item8.state, 'Shawarma Chicken')
                ItemButton:
                    id: grill_item9
                    text: 'Buffalo Chicken Tenders'
                    on_state: root.modify_list(root.itemList, grill_item9.state, 'Buffalo Chicken Tenders')
                ItemButton:
                    id: grill_item10
                    text: 'Pastrami Reuben'
                    on_state: root.modify_list(root.itemList, grill_item10.state, 'Pastrami Reuben')
                ItemButton:
                    id: grill_item11
                    text: 'Deli Sandwich'
                    on_state: root.modify_list(root.itemList, grill_item11.state, 'Deli Sandwich')
                ItemButton:
                    id: grill_item12
                    text: 'Tuna Melt'
                    on_state: root.modify_list(root.itemList, grill_item12.state, 'Tuna Melt')
                ItemButton:
                    id: grill_item13
                    text: 'Grilled Cheese'
                    on_state: root.modify_list(root.itemList, grill_item13.state, 'Grilled Cheese')
                ItemButton:
                    id: grill_item14
                    text: 'Grilled Cheese w/ Tomato'
                    on_state: root.modify_list(root.itemList, grill_item14.state, 'Grilled Cheese w/ Tomato')
                ItemButton:
                    id: grill_item15
                    text: 'Grilled Cheese w/ Bacon'
                    on_state: root.modify_list(root.itemList, grill_item15.state, 'Grilled Cheese w/ Bacon')
                SubmenuButton:
                    id: beverages
                    text: 'Beverages'
                    on_state: root.modify_state(beverages.state, 'beverages', 5)
                ItemButton:
                    id: beverages_item1
                    text: 'Smoothie'
                    on_state: root.modify_list(root.itemList, beverages_item1.state, 'Smoothie')
                ItemButton:
                    id: beverages_item2
                    text: 'Smoothie w/ Protein Powder'
                    on_state: root.modify_list(root.itemList, beverages_item2.state, 'Smoothie w/ Protein Powder')
                ItemButton:
                    id: beverages_item3
                    text: 'Frost'
                    on_state: root.modify_list(root.itemList, beverages_item3.state, 'Frost')
                ItemButton:
                    id: beverages_item4
                    text: 'Small Gelato'
                    on_state: root.modify_list(root.itemList, beverages_item4.state, 'Small Gelato')
                ItemButton:
                    id: beverages_item5
                    text: 'Large Gelato'
                    on_state: root.modify_list(root.itemList, beverages_item5.state, 'Large Gelato')
                SubmenuButton:
                    id: vegan
                    text: 'Salad & Vegan'
                    on_state: root.modify_state(vegan.state, 'vegan', 11)
                ItemButton:
                    id: vegan_item1
                    text: 'Dinner Salad'
                    on_state: root.modify_list(root.itemList, vegan_item1.state, 'Dinner Salad')
                ItemButton:
                    id: vegan_item2
                    text: 'Side Salad'
                    on_state: root.modify_list(root.itemList, vegan_item2.state, 'Side Salad')
                ItemButton:
                    id: vegan_item3
                    text: 'Pita w/ Hummus'
                    on_state: root.modify_list(root.itemList, vegan_item3.state, 'Pita w/ Hummus')
                ItemButton:
                    id: vegan_item4
                    text: 'Veggie Pocket'
                    on_state: root.modify_list(root.itemList, vegan_item4.state, 'Veggie Pocket')
                ItemButton:
                    id: vegan_item5
                    text: 'Chicken Caesar'
                    on_state: root.modify_list(root.itemList, vegan_item5.state, 'Chicken Caesar')
                ItemButton:
                    id: vegan_item6
                    text: 'Side of Hummus'
                    on_state: root.modify_list(root.itemList, vegan_item6.state, 'Side of Hummus')
                ItemButton:
                    id: vegan_item7
                    text: 'Mac n Cheese'
                    on_state: root.modify_list(root.itemList, vegan_item7.state, 'Mac n Cheese')
                ItemButton:
                    id: vegan_item8
                    text: 'Falafel'
                    on_state: root.modify_list(root.itemList, vegan_item8.state, 'Falafel')
                ItemButton:
                    id: vegan_item9
                    text: 'Veggie Burrito'
                    on_state: root.modify_list(root.itemList, vegan_item9.state, 'Veggie Burrito')
                ItemButton:
                    id: vegan_item10
                    text: 'Garden Burger'
                    on_state: root.modify_list(root.itemList, vegan_item10.state, 'Garden Burger')
                ItemButton:
                    id: vegan_item11
                    text: 'Vegan Quesadilla'
                    on_state: root.modify_list(root.itemList, vegan_item11.state, 'Vegan Quesadilla')
<LeesMenu>:
    carte: carte
    beverages: beverages
    desserts: desserts
    on_enter:
        root.itemList = root.initialize_list()
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "home_screen"
                root.carte.state = 'normal'
                root.beverages.state = 'normal'
                root.desserts.state = 'normal'
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                root.manager.get_screen('length_exact').itemList = root.itemList
                root.manager.get_screen('length_range').itemList = root.itemList
                root.manager.get_screen('price_exact').itemList = root.itemList
                root.manager.get_screen('price_range').itemList = root.itemList
                root.manager.get_screen('more_exact').itemList = root.itemList
                root.manager.get_screen('more_exact_two').itemList = root.itemList
                root.manager.get_screen('more_range').itemList = root.itemList
                root.manager.get_screen('more_range_two').itemList = root.itemList
                root.manager.get_screen('length_exact').len_exact_input.hint_text = "Integer 1-"+str(len(root.itemList.longOrder(7)))
                root.manager.get_screen('length_range').len_range_input_upper.hint_text = "Integer less than "+str((root.itemList.longestOrder(7))+1)
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 0.93}
        padding: 0, 35
        InstructionsLabel:
            text: "Select all menus and items to EXCLUDE from your order"
        ScrollView:
            GridLayout:
                cols: 1
                padding: 20
                spacing: 5
                size_hint_y: None
                height: self.minimum_height
                SubmenuButton:
                    id: carte
                    text: 'A la Carte'
                    on_state: root.modify_state(carte.state, 'carte', 18)
                ItemButton:
                    id: carte_item1
                    text: 'Egg Any Style'
                    on_state: root.modify_list(root.itemList, carte_item1.state, 'Egg Any Style')
                ItemButton:
                    id: carte_item2
                    text: 'DIY Omelet'
                    on_state: root.modify_list(root.itemList, carte_item2.state, 'DIY Omelet')
                ItemButton:
                    id: carte_item3
                    text: 'Omelet Toppings'
                    on_state: root.modify_list(root.itemList, carte_item3.state, 'Omelet Toppings')
                ItemButton:
                    id: carte_item4
                    text: 'Cheese Omelet'
                    on_state: root.modify_list(root.itemList, carte_item4.state, 'Cheese Omelet')
                ItemButton:
                    id: carte_item5
                    text: 'Bacon Ham Sausage'
                    on_state: root.modify_list(root.itemList, carte_item5.state, 'Bacon Ham Sausage')
                ItemButton:
                    id: carte_item6
                    text: 'Bagel Supreme'
                    on_state: root.modify_list(root.itemList, carte_item6.state, 'Bagel Supreme')
                ItemButton:
                    id: carte_item7
                    text: 'Egg & Bagel'
                    on_state: root.modify_list(root.itemList, carte_item7.state, 'Egg & Bagel')
                ItemButton:
                    id: carte_item8
                    text: 'Egg McWilliams'
                    on_state: root.modify_list(root.itemList, carte_item8.state, 'Egg McWilliams')
                ItemButton:
                    id: carte_item9
                    text: 'Breakfast Burrito'
                    on_state: root.modify_list(root.itemList, carte_item9.state, 'Breakfast Burrito')
                ItemButton:
                    id: carte_item10
                    text: 'Hash Browns'
                    on_state: root.modify_list(root.itemList, carte_item10.state, 'Hash Browns')
                ItemButton:
                    id: carte_item11
                    text: 'English Muffin'
                    on_state: root.modify_list(root.itemList, carte_item11.state, 'English Muffin')
                ItemButton:
                    id: carte_item12
                    text: 'Toasted Bagel'
                    on_state: root.modify_list(root.itemList, carte_item12.state, 'Toasted Bagel')
                ItemButton:
                    id: carte_item13
                    text: 'Toast'
                    on_state: root.modify_list(root.itemList, carte_item13.state, 'Toast')
                ItemButton:
                    id: carte_item14
                    text: 'Fresh Fruit Bowl'
                    on_state: root.modify_list(root.itemList, carte_item14.state, 'Fresh Fruit Bowl')
                ItemButton:
                    id: carte_item15
                    text: 'Condiments'
                    on_state: root.modify_list(root.itemList, carte_item15.state, 'Condiments')
                ItemButton:
                    id: carte_item16
                    text: 'Belgian Waffle'
                    on_state: root.modify_list(root.itemList, carte_item16.state, 'Belgian Waffle')
                ItemButton:
                    id: carte_item17
                    text: '3 Pancakes'
                    on_state: root.modify_list(root.itemList, carte_item17.state, '3 Pancakes')
                ItemButton:
                    id: carte_item18
                    text: 'Pancake Toppings'
                    on_state: root.modify_list(root.itemList, carte_item18.state, 'Pancake Toppings')
                SubmenuButton:
                    id: beverages
                    text: 'Beverages'
                    on_state: root.modify_state(beverages.state, 'beverages', 12)
                ItemButton:
                    id: beverages_item1
                    text: 'Coffee'
                    on_state: root.modify_list(root.itemList, beverages_item1.state, 'Coffee')
                ItemButton:
                    id: beverages_item2
                    text: 'Hot Tea'
                    on_state: root.modify_list(root.itemList, beverages_item2.state, 'Hot Tea')
                ItemButton:
                    id: beverages_item3
                    text: 'Hot Chocolate'
                    on_state: root.modify_list(root.itemList, beverages_item3.state, 'Hot Chocolate')
                ItemButton:
                    id: beverages_item4
                    text: 'Latte'
                    on_state: root.modify_list(root.itemList, beverages_item4.state, 'Latte')
                ItemButton:
                    id: beverages_item5
                    text: 'Cappuccino'
                    on_state: root.modify_list(root.itemList, beverages_item5.state, 'Cappuccino')
                ItemButton:
                    id: beverages_item6
                    text: 'Espresso'
                    on_state: root.modify_list(root.itemList, beverages_item6.state, 'Espresso')
                ItemButton:
                    id: beverages_item7
                    text: 'Double Espresso'
                    on_state: root.modify_list(root.itemList, beverages_item7.state, 'Double Espresso')
                ItemButton:
                    id: beverages_item8
                    text: 'Juice'
                    on_state: root.modify_list(root.itemList, beverages_item8.state, 'Juice')
                ItemButton:
                    id: beverages_item9
                    text: 'Milk'
                    on_state: root.modify_list(root.itemList, beverages_item9.state, 'Milk')
                ItemButton:
                    id: beverages_item10
                    text: 'Soy Milk'
                    on_state: root.modify_list(root.itemList, beverages_item10.state, 'Soy Milk')
                ItemButton:
                    id: beverages_item11
                    text: 'Soda'
                    on_state: root.modify_list(root.itemList, beverages_item11.state, 'Soda')
                ItemButton:
                    id: beverages_item12
                    text: 'Frost'
                    on_state: root.modify_list(root.itemList, beverages_item12.state, 'Frost')
                SubmenuButton:
                    id: desserts
                    text: 'Desserts'
                    on_state: root.modify_state(desserts.state, 'desserts', 6)
                ItemButton:
                    id: desserts_item1
                    text: 'Honey Bun'
                    on_state: root.modify_list(root.itemList, desserts_item1.state, 'Honey Bun')
                ItemButton:
                    id: desserts_item2
                    text: 'A la Mode'
                    on_state: root.modify_list(root.itemList, desserts_item2.state, 'A la Mode')
                ItemButton:
                    id: desserts_item3
                    text: 'Small Gelato'
                    on_state: root.modify_list(root.itemList, desserts_item3.state, 'Small Gelato')
                ItemButton:
                    id: desserts_item4
                    text: 'Large Gelato'
                    on_state: root.modify_list(root.itemList, desserts_item4.state, 'Large Gelato')
                ItemButton:
                    id: desserts_item5
                    text: 'Small Ice Cream'
                    on_state: root.modify_list(root.itemList, desserts_item5.state, 'Small Ice Cream')
                ItemButton:
                    id: desserts_item6
                    text: 'Large Ice Cream'
                    on_state: root.modify_list(root.itemList, desserts_item6.state, 'Large Ice Cream')
<EcoCafeMenu>:
    bakery: bakery
    breakfast: breakfast
    grab: grab
    beverages: beverages
    snacks: snacks
    on_enter:
        root.itemList = root.initialize_list()
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "home_screen"
                root.bakery.state = 'normal'
                root.breakfast.state = 'normal'
                root.grab.state = 'normal'
                root.beverages.state = 'normal'
                root.snacks.state = 'normal'
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                root.manager.get_screen('length_exact').itemList = root.itemList
                root.manager.get_screen('length_range').itemList = root.itemList
                root.manager.get_screen('price_exact').itemList = root.itemList
                root.manager.get_screen('price_range').itemList = root.itemList
                root.manager.get_screen('more_exact').itemList = root.itemList
                root.manager.get_screen('more_exact_two').itemList = root.itemList
                root.manager.get_screen('more_range').itemList = root.itemList
                root.manager.get_screen('more_range_two').itemList = root.itemList
                root.manager.get_screen('length_exact').len_exact_input.hint_text = "Integer 1-"+str(len(root.itemList.longOrder(7)))
                root.manager.get_screen('length_range').len_range_input_upper.hint_text = "Integer less than "+str((root.itemList.longestOrder(7))+1)
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 0.93}
        padding: 0, 35
        InstructionsLabel:
            text: "Select all menus and items to EXCLUDE from your order"
        ScrollView:
            GridLayout:
                cols: 1
                padding: 20
                spacing: 5
                size_hint_y: None
                height: self.minimum_height
                SubmenuButton:
                    id: bakery
                    text: 'Bakery'
                    on_state: root.modify_state(bakery.state, 'bakery', 7)
                ItemButton:
                    id: bakery_item1
                    text: 'Cookie'
                    on_state: root.modify_list(root.itemList, bakery_item1.state, 'Cookie')
                ItemButton:
                    id: bakery_item2
                    text: 'Biscotti'
                    on_state: root.modify_list(root.itemList, bakery_item2.state, 'Biscotti')
                ItemButton:
                    id: bakery_item3
                    text: 'Giant Muffin'
                    on_state: root.modify_list(root.itemList, bakery_item3.state, 'Giant Muffin')
                ItemButton:
                    id: bakery_item4
                    text: 'Tea Bread'
                    on_state: root.modify_list(root.itemList, bakery_item4.state, 'Tea Bread')
                ItemButton:
                    id: bakery_item5
                    text: 'Fresh Scone'
                    on_state: root.modify_list(root.itemList, bakery_item5.state, 'Fresh Scone')
                ItemButton:
                    id: bakery_item6
                    text: 'Biscuit'
                    on_state: root.modify_list(root.itemList, bakery_item6.state, 'Biscuit')
                ItemButton:
                    id: bakery_item7
                    text: 'Honey Buns'
                    on_state: root.modify_list(root.itemList, bakery_item7.state, 'Honey Buns')
                SubmenuButton:
                    id: breakfast
                    text: 'Breakfast'
                    on_state: root.modify_state(breakfast.state, 'breakfast', 6)
                ItemButton:
                    id: breakfast_item1
                    text: 'Cereal w/ Milk'
                    on_state: root.modify_list(root.itemList, breakfast_item1.state, 'Cereal w/ Milk')
                ItemButton:
                    id: breakfast_item2
                    text: 'Bagel'
                    on_state: root.modify_list(root.itemList, breakfast_item2.state, 'Bagel')
                ItemButton:
                    id: breakfast_item3
                    text: 'Bagel w/ Cream Cheese'
                    on_state: root.modify_list(root.itemList, breakfast_item3.state, 'Bagel w/ Cream Cheese')
                ItemButton:
                    id: breakfast_item4
                    text: 'Fresh Fruit'
                    on_state: root.modify_list(root.itemList, breakfast_item4.state, 'Fresh Fruit')
                ItemButton:
                    id: breakfast_item5
                    text: 'Stonyfield Yogurt'
                    on_state: root.modify_list(root.itemList, breakfast_item5.state, 'Stonyfield Yogurt')
                ItemButton:
                    id: breakfast_item6
                    text: 'Breakfast Combo'
                    on_state: root.modify_list(root.itemList, breakfast_item6.state, 'Breakfast Combo')
                SubmenuButton:
                    id: grab
                    text: "Grab 'n Go"
                    on_state: root.modify_state(grab.state, "Grab 'n Go", 3)
                ItemButton:
                    id: grab_item1
                    text: 'Sandwich'
                    on_state: root.modify_list(root.itemList, grab_item1.state, 'Sandwich')
                ItemButton:
                    id: grab_item2
                    text: 'Chef Salad'
                    on_state: root.modify_list(root.itemList, grab_item2.state, 'Chef Salad')
                ItemButton:
                    id: grab_item3
                    text: 'Soup'
                    on_state: root.modify_list(root.itemList, grab_item3.state, 'Soup')
                SubmenuButton:
                    id: beverages
                    text: 'Beverages'
                    on_state: root.modify_state(beverages.state, 'Beverages', 11)
                ItemButton:
                    id: beverages_item1
                    text: 'Small Coffee'
                    on_state: root.modify_list(root.itemList, beverages_item1.state, 'Small Coffee')
                ItemButton:
                    id: beverages_item2
                    text: 'Large Coffee'
                    on_state: root.modify_list(root.itemList, beverages_item2.state, 'Large Coffee')
                ItemButton:
                    id: beverages_item3
                    text: 'Hot Chocolate'
                    on_state: root.modify_list(root.itemList, beverages_item3.state, 'Hot Chocolate')
                ItemButton:
                    id: beverages_item4
                    text: 'Hot Tea'
                    on_state: root.modify_list(root.itemList, beverages_item4.state, 'Hot Tea')
                ItemButton:
                    id: beverages_item5
                    text: 'Mate Tea'
                    on_state: root.modify_list(root.itemList, beverages_item5.state, 'Mate Tea')
                ItemButton:
                    id: beverages_item6
                    text: 'Honest Tea'
                    on_state: root.modify_list(root.itemList, beverages_item6.state, 'Honest Tea')
                ItemButton:
                    id: beverages_item7
                    text: 'Chai Tea'
                    on_state: root.modify_list(root.itemList, beverages_item7.state, 'Chai Tea')
                ItemButton:
                    id: beverages_item8
                    text: 'Guayaki Organic Tea'
                    on_state: root.modify_list(root.itemList, beverages_item8.state, 'Guayaki Organic Tea')
                ItemButton:
                    id: beverages_item9
                    text: 'Natural Naked Juices'
                    on_state: root.modify_list(root.itemList, beverages_item9.state, 'Natural Naked Juices')
                ItemButton:
                    id: beverages_item10
                    text: 'Milk'
                    on_state: root.modify_list(root.itemList, beverages_item10.state, 'Milk')
                ItemButton:
                    id: beverages_item11
                    text: 'Bottled water'
                    on_state: root.modify_list(root.itemList, beverages_item11.state, 'Bottled water')
                SubmenuButton:
                    id: snacks
                    text: 'Snacks'
                    on_state: root.modify_state(snacks.state, 'Snacks', 4)
                ItemButton:
                    id: snacks_item1
                    text: 'Energy bars'
                    on_state: root.modify_list(root.itemList, snacks_item1.state, 'Energy bars')
                ItemButton:
                    id: snacks_item2
                    text: 'Endangered bars'
                    on_state: root.modify_list(root.itemList, snacks_item2.state, 'Endangered bars')
                ItemButton:
                    id: snacks_item3
                    text: 'Trail Mix'
                    on_state: root.modify_list(root.itemList, snacks_item3.state, 'Trail Mix')
                ItemButton:
                    id: snacks_item4
                    text: 'Mixed Fruit & Nut'
                    on_state: root.modify_list(root.itemList, snacks_item4.state, 'Mixed Fruit & Nut')
<ToolScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Home"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "home_screen"
                root.manager.get_screen('whitmans_menu').fryer.state = 'normal'
                root.manager.get_screen('whitmans_menu').grill.state = 'normal'
                root.manager.get_screen('whitmans_menu').beverages.state = 'normal'
                root.manager.get_screen('whitmans_menu').vegan.state = 'normal'
                root.manager.get_screen('lees_menu').carte.state = 'normal'
                root.manager.get_screen('lees_menu').beverages.state = 'normal'
                root.manager.get_screen('lees_menu').desserts.state = 'normal'
                root.manager.get_screen('ecocafe_menu').bakery.state = 'normal'
                root.manager.get_screen('ecocafe_menu').breakfast.state = 'normal'
                root.manager.get_screen('ecocafe_menu').grab.state = 'normal'
                root.manager.get_screen('ecocafe_menu').beverages.state = 'normal'
                root.manager.get_screen('ecocafe_menu').snacks.state = 'normal'
        DirectionButton:
            text: "Help"
            pos_hint: {'center_x': 0.5, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "help_screen"
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 0.93}
        padding: 0, 35
        InstructionsLabel:
            text: "Select a tool"
        ScrollView:
            GridLayout:
                cols: 1
                padding: 20
                spacing: 5
                size_hint_y: None
                height: self.minimum_height
                ToolButton:
                    text: "Exact Length Order"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "length_exact"
                ToolButton:
                    text: "Length Range Order"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "length_range"
                ToolButton:
                    text: "Exact Price Order"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "price_exact"
                ToolButton:
                    text: "Price Range Order"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "price_range"
                ToolButton:
                    text: "Partial Order w/ Exact Price"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "more_exact"
                ToolButton:
                    text: "Partial Order w/ Price Range"
                    on_press:
                        root.manager.transition.duration = 0
                        root.manager.current = "more_range"
<HelpScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 0.93}
        padding: 0, 35
        InstructionsLabel:
            text: "The Tools"
        ScrollView:
            GridLayout:
                cols: 1
                padding: 20
                spacing: 5
                size_hint_y: None
                height: self.minimum_height
                OrderLabel:
                    text: "Exact Length Order"
                SubLabel:
                    text: "Say that you don't really care about how much you spend, but you want to order exactly 3 things. This tool will give you all possible orders containing some exact number of items."
                OrderLabel:
                    text: "Length Range Order"
                SubLabel:
                    text: "Works the same as 'Exact Length Order' but allows you to specify a range of order lengths, for example all orders containing 2-4 items."
                OrderLabel:
                    text: "Exact Price Order"
                SubLabel:
                    text: "Say that you DO really care about how much you spend, and you want to use all $7.00 on your meal swipe. This tool will give you all possible orders that cost some exact price."
                OrderLabel:
                    text: "Price Range Order"
                SubLabel:
                    text: "Works the same as 'Price Range Order' but allows you to specify a price range, like all orders that cost between $6.50 and $7.00."
                OrderLabel:
                    text: "Partial Order w/ Exact Price"
                SubLabel:
                    text: "Say that there are a couple things on the menu that you already know you want to order. This tool allows you to specify those items and tells you what else you can order with the rest of your money so that the total adds up to some exact price."
                OrderLabel:
                    text: "Partial Order w/ Price Range"
                SubLabel:
                    text: "Works the same as 'Partial Order w/ Exact Price' but allows you to specify a total price range."
<LengthExact>:
    len_exact_input: len_exact_input
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, int(len_exact_input.text))
                except ValueError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter the number of items you want to order"
            TextInput:
                id: len_exact_input
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                hint_text: ""
                padding_x: [20,0]
<LengthRange>:
    len_range_input_upper: len_range_input_upper
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, int(len_range_input_lower.text), int(len_range_input_upper.text))
                except ValueError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter the lower bound number of items you want to order"
            TextInput:
                id: len_range_input_lower
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
            InstructionsLabel:
                text: "Enter the upper bound number of items you want to order"
            TextInput:
                id: len_range_input_upper
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                hint_text: ""
                padding_x: [20,0]
<PriceExact>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, float(eval(price_exact_input.text)))
                except SyntaxError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter what you want the total price of your order to be"
            SubLabel:
                text: 'Must not exceed $7.00. Do not include a dollar sign'
            TextInput:
                id: price_exact_input
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
<PriceRange>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, float(eval(price_range_input_lower.text)), float(eval(price_range_input_upper.text)))
                except SyntaxError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter a lower total price for your order"
            SubLabel:
                text: 'Must not exceed $7.00. Do not include a dollar sign'
            TextInput:
                id: price_range_input_lower
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
            InstructionsLabel:
                text: "Enter an upper bound total price for your order"
            SubLabel:
                text: "Must be greater than the lower bound"
            TextInput:
                id: price_range_input_upper
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
<MoreExact>:
    more_exact_remaining: more_exact_remaining
    on_enter:
        more_exact_remaining.text = "Amount remaining: $7.00"
        root.initialOrder = root.initialize_initial_order()
        root.initial_order(root.itemList)
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                root.manager.get_screen('more_exact_two').more_exact_two.text = "Must be between $"+"{0:.2f}".format(7-float(more_exact_remaining.text[-4:]))+" and $7.00. Do not include a dollar sign"
                root.manager.get_screen('more_exact_two').initialOrder = root.initialOrder
                root.manager.transition.duration = 0
                root.manager.current = "more_exact_two"
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        InstructionsLabel:
            text: "Select all items to include in your order"
        SubLabel:
            id: more_exact_remaining
            text: "Amount remaining: $7.00"
<MoreExactTwo>:
    more_exact_two: more_exact_two
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "more_exact"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, root.initialOrder, float(eval(more_exact_input.text)))
                except SyntaxError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter what you want the total price of your order to be"
            SubLabel:
                id: more_exact_two
                text: ''
            TextInput:
                id: more_exact_input
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
<MoreRange>:
    more_range_remaining: more_range_remaining
    on_enter:
        more_range_remaining.text = "Amount remaining: $7.00"
        root.initialOrder = root.initialize_initial_order()
        root.initial_order(root.itemList)
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "tool_screen"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                root.manager.get_screen('more_range_two').more_range_two.text = "Must be between $"+"{0:.2f}".format(7-float(more_range_remaining.text[-4:]))+" and $7.00. Do not include a dollar sign"
                root.manager.get_screen('more_range_two').initialOrder = root.initialOrder
                root.manager.transition.duration = 0
                root.manager.current = "more_range_two"
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        InstructionsLabel:
            text: "Select all items to include in your order"
        SubLabel:
            id: more_range_remaining
            text: "Amount remaining: $7.00"
<MoreRangeTwo>:
    more_range_two: more_range_two
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        DirectionButton:
            text: "Back"
            pos_hint: {'left': 1, 'top': 1}
            on_press:
                root.manager.transition.duration = 0
                root.manager.current = "more_range"
        DirectionButton:
            text: "Done"
            pos_hint: {'right': 1, 'top': 1}
            on_press:
                try: root.compute_orders(root.itemList, root.initialOrder, float(eval(more_range_input_lower.text)), float(eval(more_range_input_upper.text)))
                except SyntaxError: pass
    GridLayout:
        cols: 1
        pos_hint: {'top': 0.86}
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
            InstructionsLabel:
                text: "Enter a lower total price for your order"
            SubLabel:
                id: more_range_two
                text: ''
            TextInput:
                id: more_range_input_lower
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
            InstructionsLabel:
                text: "Enter an upper bound total price for your order"
            SubLabel:
                text: "Must be greater than lower bound"
            TextInput:
                id: more_range_input_upper
                size_hint: None, None
                width: 300
                height: 35
                multiline: False
                padding_x: [20,0]
''')

class DiningButton(Button):
    pass

class DirectionButton(Button):
    pass

class SubmenuButton(ToggleButton):
    pass

class ItemButton(ToggleButton):
    pass

class InitialOrderButton(Button):
    pass

class ToolButton(Button):
    pass

class InstructionsLabel(Label):
    pass

class SubLabel(Label):
    pass

class OrderLabel(Label):
    pass

class HomeScreen(Screen):
    pass

class WhitmansMenu(Screen):
    itemList = Menu()

    def initialize_list(self):
        itemList = Menu('whitmans')
        global allItems
        allItems = itemList.getCopy()
        return itemList

    def modify_list(self, itemList, value, dish):
        if value == 'down':
            for item in itemList:
                if dish == item.getDish():
                    itemList.remove(item)
                    break
        else:
            for item in allItems:
                if dish == item.getDish():
                    itemList.append(item)
                    break

    def modify_state(self, value, submenu, length):
        if value == 'down':
            for i in range(1, length+1):
                button = self.ids[str(submenu)+'_item'+str(i)]
                button.state = 'down'
        else:
            for i in range(1, length+1):
                button = self.ids[str(submenu)+'_item'+str(i)]
                button.state = 'normal'

class LeesMenu(Screen):
    itemList = Menu()

    def initialize_list(self):
        itemList = Menu('lees')
        global allItems
        allItems = itemList.getCopy()
        return itemList

    def modify_list(self, itemList, value, dish):
        if value == 'down':
            for item in itemList:
                if dish == item.getDish():
                    itemList.remove(item)
                    break
        else:
            for item in allItems:
                if dish == item.getDish():
                    itemList.append(item)
                    break

    def modify_state(self, value, submenu, length):
        if value == 'down':
            for i in range(1, length + 1):
                button = self.ids[str(submenu) + '_item' + str(i)]
                button.state = 'down'
        else:
            for i in range(1, length + 1):
                button = self.ids[str(submenu) + '_item' + str(i)]
                button.state = 'normal'

class EcoCafeMenu(Screen):
    itemList = Menu()

    def initialize_list(self):
        itemList = Menu('ecocafe')
        global allItems
        allItems = itemList.getCopy()
        return itemList

    def modify_list(self, itemList, value, dish):
        if value == 'down':
            for item in itemList:
                if dish == item.getDish():
                    itemList.remove(item)
                    break
        else:
            for item in allItems:
                if dish == item.getDish():
                    itemList.append(item)
                    break

    def modify_state(self, value, submenu, length):
        if value == 'down':
            for i in range(1, length + 1):
                button = self.ids[str(submenu) + '_item' + str(i)]
                button.state = 'down'
        else:
            for i in range(1, length + 1):
                button = self.ids[str(submenu) + '_item' + str(i)]
                button.state = 'normal'

class ToolScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class LengthExact(Screen):
    itemList = Menu()

    def compute_orders(self, itemList, length):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.86}, padding=(0, 80))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.lengthExact(length)
                for order in result:
                    temp = Menu()
                    for item in order:
                        temp.append(item)
                    grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class LengthRange(Screen):
    itemList = Menu()

    def compute_orders(self, itemList, lower, upper):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.8}, padding=(0, 115))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.lengthRange(lower, upper)
                for order in result:
                    temp = Menu()
                    for item in order:
                        temp.append(item)
                    grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class PriceExact(Screen):
    itemList = Menu()

    def compute_orders(self, itemList, price):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.8}, padding=(0, 115))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.priceExact(price)
                if len(result) == 0:
                    grid.add_widget(OrderLabel(text='No results. Try different parameters!'))
                else:
                    for order in result:
                        temp = Menu()
                        if len(order) == 1:
                            temp.append(order)
                        else:
                            for item in order:
                                temp.append(item)
                        grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class PriceRange(Screen):
    itemList = Menu()

    def compute_orders(self, itemList, lower, upper):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.75}, padding=(0, 145))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.priceRange(lower, upper)
                if len(result) == 0:
                    grid.add_widget(OrderLabel(text='No results. Try different parameters!'))
                else:
                    for order in result:
                        temp = Menu()
                        if len(order) == 1:
                            temp.append(order)
                        else:
                            for item in order:
                                temp.append(item)
                        grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class MoreExact(Screen):
    itemList = Menu()

    def initialize_initial_order(self):
        global initialOrder
        initialOrder = []
        return initialOrder

    def modify_initial_order(self, item, keywords):
        initialCost = 0
        for dish in initialOrder:
            initialCost += dish.getPrice()
        if initialCost + item.getPrice() <= 7:
            initialCost += item.getPrice()
            initialOrder.append(item)
        self.more_exact_remaining.text = "Amount remaining: $"+"{0:.2f}".format(7.00-initialCost)

    def initial_order(self, itemList):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.88}, padding=(0, 75))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            for item in itemList:
                btn = InitialOrderButton(text=str(item.getDish()))
                btncallback = partial(self.modify_initial_order, item)
                btn.bind(on_press=btncallback)
                grid.add_widget(btn)
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class MoreExactTwo(Screen):
    itemList = Menu()
    initialOrder = []

    def compute_orders(self, itemList, initialOrder, price):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.84}, padding=(0, 100))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.moreExact(initialOrder, price)
                if len(result) == 0:
                    grid.add_widget(OrderLabel(text='No results. Try different parameters!'))
                else:
                    for order in result:
                        temp = Menu()
                        if len(order) == 1:
                            temp.append(order)
                        else:
                            for item in order:
                                temp.append(item)
                        grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class MoreRange(Screen):
    itemList = Menu()

    def initialize_initial_order(self):
        global initialOrder
        initialOrder = []
        return initialOrder

    def modify_initial_order(self, item, keywords):
        initialCost = 0
        for dish in initialOrder:
            initialCost += dish.getPrice()
        if initialCost + item.getPrice() <= 7:
            initialCost += item.getPrice()
            initialOrder.append(item)
        self.more_range_remaining.text = "Amount remaining: $"+"{0:.2f}".format(7.00-initialCost)

    def initial_order(self, itemList):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.88}, padding=(0, 75))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            for item in itemList:
                btn = InitialOrderButton(text=str(item.getDish()))
                btncallback = partial(self.modify_initial_order, item)
                btn.bind(on_press=btncallback)
                grid.add_widget(btn)
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)

class MoreRangeTwo(Screen):
    itemList = Menu()
    initialOrder = []

    def compute_orders(self, itemList, initialOrder, lower, upper):
        for c in list(self.children):
            if isinstance(c, BoxLayout): self.remove_widget(c)
        else:
            box = BoxLayout(orientation='vertical', pos_hint={'top': 0.75}, padding=(0, 145))
            grid = GridLayout(cols=1, padding=20, spacing=5, size_hint_y=None)
            grid.bind(minimum_height=grid.setter('height'))
            try:
                result = itemList.moreRange(initialOrder, lower, upper)
                if len(result) == 0:
                    grid.add_widget(OrderLabel(text='No results. Try different parameters!'))
                else:
                    for order in result:
                        temp = Menu()
                        if len(order) == 1:
                            temp.append(order)
                        else:
                            for item in order:
                                temp.append(item)
                        grid.add_widget(OrderLabel(text=temp.getDishes()))
            except AssertionError:
                grid.add_widget(OrderLabel(text='Bound error. Try different parameters!'))
            sv = ScrollView(do_scroll_x=False)
            box.add_widget(sv)
            sv.add_widget(grid)
            self.add_widget(box)


screen_manager = ScreenManager()
screen_manager.add_widget(HomeScreen(name="home_screen"))
screen_manager.add_widget(WhitmansMenu(name="whitmans_menu"))
screen_manager.add_widget(LeesMenu(name="lees_menu"))
screen_manager.add_widget(EcoCafeMenu(name="ecocafe_menu"))
screen_manager.add_widget(ToolScreen(name="tool_screen"))
screen_manager.add_widget(HelpScreen(name="help_screen"))
screen_manager.add_widget(LengthExact(name="length_exact"))
screen_manager.add_widget(LengthRange(name="length_range"))
screen_manager.add_widget(PriceExact(name="price_exact"))
screen_manager.add_widget(PriceRange(name="price_range"))
screen_manager.add_widget(MoreExact(name="more_exact"))
screen_manager.add_widget(MoreExactTwo(name='more_exact_two'))
screen_manager.add_widget(MoreRange(name="more_range"))
screen_manager.add_widget(MoreRangeTwo(name='more_range_two'))


class SnartoolsApp(App):

    def build(self):
        return screen_manager


app = SnartoolsApp()
app.run()
