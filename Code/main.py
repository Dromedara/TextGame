import Code.BasicFuncs.Start.StartGame as StartGame
from Code.BasicFuncs.Finish.FinishGame import finish_it
from Code.BasicFuncs.Game.Warehouse import EquippingRunner
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.BasicFuncs.Game.Warehouse.Inventory.Battle import battle_inventory
import Code.BasicFuncs.Game.Shop.Buying as Buying
from Code.BasicFuncs.Game.Shop import Sellers
from Code.Classes.MainHero.Savior import ReadHero
import Code.BasicFuncs.Game.Guild.GuildHall as GuildHall

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


StartGame.start_it(first_activation=False)


class MainMenu(Screen):
    size_hint = (0.5, 0.5)

    def exit(self):
        finish_it()
    pass


class GameMenu(Screen):
    size_hint = (0.5, 0.5)


class JustSettings(Screen):
    pass


class GuildMenu(Screen):
    size_hint = (0.5, 0.5)
    monster = ""
    class MissionButton(Button):
        pass
    def ShowMissions(self):
        list_of_missions = GuildHall.all_adventures()
        for i in list_of_missions:
            n = self.MissionButton(text= str(i[0]) + " " + str(i[1]))
            n.id = i[0]
            self.ids.list.add_widget(n)

    pass


class BattleMenu(Screen):
    size_hint = (0.5, 0.5)

    def change_battle_log(self, text):
        self.ids.battle_label.text = str(text) + '\n' + self.ids.battle_label.text

    def clear_battle_log(self):
        self.ids.battle_label.text += ''
    pass


class Inventory(Screen):

    class ItemButton(Button):
        pass

    def equip_item(self, _id):
        _id = int(_id)
        EquippingRunner.put_it_on(_id)

    def unequip_item(self, _id):
        _id = int(_id)
        EquippingRunner.put_it_off(_id)
        self.show_equipment()

    def create_description(self, _name, _id):
        self.ids.description_label.text = str(_name)
        self.ids.description_label.name = str(_id)

    def show_equipment(self):
        self.ids.here.clear_widgets()
        self.ids.description_label.text = ""
        self.ids.description_label.name = ""
        self.ids.show_equipment.state = "down"
        self.ids.show_artefacts.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_armour.state = "normal"
        self.ids.equip_button.text = "Unequip"
        items_in_shop = battle_inventory.get_potions()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)
        items_in_shop = battle_inventory.get_armors()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)
        items_in_shop = battle_inventory.get_artefacts()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)

    def show_armour(self):
        self.ids.description_label.text = ""
        self.ids.description_label.name = ""
        self.ids.here.clear_widgets()
        self.ids.show_artefacts.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_equipment.state = "normal"
        self.ids.show_armour.state = "down"
        self.ids.equip_button.text = "Equip"
        items_in_shop = main_inventory.get_armors()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)

    def show_artefacts(self):
        self.ids.description_label.text = ""
        self.ids.description_label.name = ""
        self.ids.here.clear_widgets()
        self.ids.show_armour.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_equipment.state = "normal"
        self.ids.show_artefacts.state = "down"
        self.ids.equip_button.text = "Equip"
        items_in_shop = main_inventory.get_artefacts()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)

    def show_potions(self):
        self.ids.description_label.text = ""
        self.ids.description_label.name = ""
        self.ids.here.clear_widgets()
        self.ids.show_artefacts.state = "normal"
        self.ids.show_armour.state = "normal"
        self.ids.show_equipment.state = "normal"
        self.ids.show_potions.state = "down"
        self.ids.equip_button.text = "Equip"
        items_in_shop = main_inventory.get_potions()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)

    def clear_buttons(self):
        self.ids.here.clear_widgets()
    pass


class Shop(Screen):
    class ShopItemButton(Button):
        pass
    def amount_of_gold(self):
        gold = str(ReadHero.read_it().gold)
        return gold

    def create_description(self, _name, _id):
        self.ids.description_label.text = str(_name)
        self.ids.description_label.name = str(_id)

    def buy_armor(self, _id):
        Buying.buy_armor(int(_id))

    def buy_artefact(self, _id):
        Buying.buy_artefact(int(_id))

    def buy_potion(self, _id):
        Buying.buy_potion(int(_id))

    def show_armour(self):
        self.ids.here.clear_widgets()
        self.ids.show_artefacts.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_armour.state = "down"
        for key in Sellers.selling_armors.keys():
            for i in Sellers.selling_armors[key].keys():
                n = self.ShopItemButton(size=(125, 125), text=str(Sellers.selling_armors[key][i].key) + "\nCost: " + str(Sellers.selling_armors[key][i].cost))
                n.id = Sellers.selling_armors[key][i].id
                self.ids.here.add_widget(n)

    def show_artefacts(self):
        self.ids.here.clear_widgets()
        self.ids.show_armour.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_artefacts.state = "down"
        for i in Sellers.selling_artefacts:
            n = self.ShopItemButton(size=(125, 125), text=str(Sellers.selling_artefacts[i].key) + "\nCost: " + str(Sellers.selling_artefacts[i].cost))
            n.id = Sellers.selling_artefacts[i].id
            self.ids.here.add_widget(n)

    def show_potions(self):
        self.ids.show_artefacts.state = "normal"
        self.ids.show_armour.state = "normal"
        self.ids.show_potions.state = "down"
        self.ids.here.clear_widgets()
        for i in Sellers.selling_potions:
            n = self.ShopItemButton(size=(125, 125), text=str(Sellers.selling_potions[i].key) + "\nCost: " + str(Sellers.selling_potions[i].cost))
            n.id = Sellers.selling_potions[i].id
            self.ids.here.add_widget(n)

    def clear_buttons(self):
        self.ids.here.clear_widgets()
        pass
    pass


class Item_from_inventory(Screen):
    size_hint = (0.5, 0.5)
    pass


class Item_from_shop(Screen):
    size_hint = (0.5, 0.5)
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('kivy_fail.kv')


class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()

