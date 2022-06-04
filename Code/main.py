import Code.BasicFuncs.Start.StartGame as StartGame
from Code.BasicFuncs.Finish.FinishGame import finish_it
from Code.BasicFuncs.Game.Warehouse import EquippingRunner
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.BasicFuncs.Game.Warehouse.Inventory import Battle
import Code.BasicFuncs.Game.Shop.Buying as Buying
from Code.BasicFuncs.Game.Shop import Sellers
from Code.Classes.MainHero.Savior import ReadHero
import Code.BasicFuncs.Game.Guild.GuildHall as GuildHall
from Code.BasicFuncs.Game.BattelField.StartBattle import Preparing
from Code.BasicFuncs.Game.BattelField.SubFuncs.DrinkingPotions import Drinking
from Code.BasicFuncs.Game.BattelField.BattleFuncs import ActiveActions, MonsterActions, PassiveActions
import time

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


StartGame.start_it(first_activation=False)


class MainMenu(Screen):
    """Creating start menu

    """
    size_hint = (0.5, 0.5)

    @staticmethod
    def exit():
        """End game

        :return: None
        """
        finish_it()
    pass


class GameMenu(Screen):
    """Creating game menu

    """
    size_hint = (0.5, 0.5)


class JustSettings(Screen):
    """Going to settings menu

    """
    pass


class GuildMenu(Screen):
    """Creating ad running guild menu.

    """
    size_hint = (0.5, 0.5)

    class MissionButton(Button):
        pass

    def start_mission(self, _name):
        """Start the mission

        :param _name: name of mission
        :return: None


        """
        BattleMenu.monster = Preparing.prepare_monster(_name)

    def ShowMissions(self):
        """Show list of missions

        :return: None


        """
        list_of_missions = GuildHall.all_adventures()
        for i in list_of_missions:
            n = self.MissionButton(text=str(i[0]) + " " + str(i[1]))
            n.name = i[0]
            self.ids.list.add_widget(n)
    pass


class BattleMenu(Screen):
    """Creating anf running battle menu


    """
    size_hint = (0.5, 0.5)
    monster = ""
    battle_hero = ''

    class StartBattleButton(Button):
        pass

    class SkillButton(Button):
        pass

    class PotionButton(Button):
        pass

    def remove(self, _id):
        """Remove widget

        :param _id: id of widget
        :return: None
        """
        self.ids.remove_widget(_id)

    def start_the_battle(self):
        """Start the battle

        :return: None
        """
        self.battle_hero = Preparing.prepare_hero()
        self.add_skill_buttons()
        self.add_potion_buttons()
        self.show_characters()
        self.ids.hero_hp.max = self.battle_hero.hp
        self.ids.monster_hp.max = self.monster.hp

    def all_for_start(self):
        """Prepearing screen for battle

        :return: None


        """
        n = self.StartBattleButton(text = "Start battle")
        n.size_hint = 2, 2
        n.size = (self.width, self.height)
        self.add_widget(n)

    def change_battle_log(self, text):
        """Changing battle logs during th battle

        :param text: text fot changing
        :return: None


        """
        self.ids.battle_label.text = str(text) + '\n' + self.ids.battle_label.text
        self.ids.hero_hp.value = self.battle_hero.hp
        self.ids.monster_hp.value = self.monster.hp

    def clear_battle_log(self):
        """Clear battle logs

        :return: None


        """
        self.ids.battle_label.text = ''

    def add_skill_buttons(self):
        """Add buttons of attacks on screen

        :return: None


        """
        self.ids.list_of_actions.clear_widgets()
        list_of_actions = self.battle_hero.hero_active_skills['artefacts'] + self.battle_hero.hero_active_skills['basic']
        for i in list_of_actions:
            n = self.SkillButton(text=str(i))
            n.id = str(i)
            self.ids.list_of_actions.add_widget(n)
        pass

    def add_potion_buttons(self):
        """Add buttons of potions on screen

        :return: None


        """
        self.ids.list_of_potions.clear_widgets()
        print(Battle.battle_inventory.curr_potions)
        list_of_potions = Battle.battle_inventory.curr_potions.values()
        print(list_of_potions)
        for i in list_of_potions:
            n = self.PotionButton(text=str(i.key))
            n.name = str(i.id)
            n.id = str(i.id)
            self.ids.list_of_potions.add_widget(n)
        pass

    def active_skill(self, _skill):
        """Run attack after clicking the button

        :param _skill: name of skill
        :return: None


        """
        if self.battle_hero.hp > 0:
            ActiveActions.run_it(self.battle_hero, self.monster, _skill)
            self.change_battle_log(f"Main hero attack: {_skill} \n")
            self.show_characters()
        if self.monster.hp > 0:
            MonsterActions.run_it(self.battle_hero, self.monster)
            self.change_battle_log(f"Monster attack \n")
            self.show_characters()
        if self.battle_hero.hp > 0 and self.monster.hp > 0:
            PassiveActions.run_it(self.battle_hero, self.monster)
            time.sleep(0.2)
            self.change_battle_log(f"Activate passives \n")
            self.show_characters()
        self.check_for_result()

    def drink_potion(self, _name, _potion):
        """Run driking potion after clicking the button.

        :param _name: name of potion.
        :param _potion: id of potion
        :return: None


        """
        self.battle_hero, changed = Drinking.drink_potion(self.battle_hero, _potion)
        if changed:
            self.change_battle_log(f"Main hero have drunk {_name} \n")
            self.battle_reequip(int(_potion))
        self.check_for_result()

    @staticmethod
    def battle_reequip(_potion):
        """Reequip equipped.

        :param _potion: id of the potion drunk
        :return: None


        """
        Battle.done_potions.append(_potion)
        del Battle.battle_inventory.curr_potions[_potion]

    def show_characters(self):
        """Show characters param in a text log.

        :return: None


        """
        status_chr = f"     Hero | Monster\nattack: {self.battle_hero.attack} | {self.monster.attack},\ndefence: {self.battle_hero.defence} | {self.monster.defence},\nmana: {self.battle_hero.mana} | {self.monster.mana},\nmagic attack: {self.battle_hero.magic_attack} | {self.monster.magic_attack}\n"
        self.change_battle_log(status_chr)
        pass

    def check_for_result(self):
        """Check hps of hero and monster. If someone died, run end of battle.

        :return: None


        """
        if self.monster.hp <= 0 and self.battle_hero.hp <= 0:
            self.end_of_battle("draw")
        elif self.monster.hp <= 0:
            self.end_of_battle("win")
        elif self.battle_hero.hp <= 0:
            self.end_of_battle("lose")

    def end_of_battle(self, result):
        """Prepare fot ending of battle.

        :param result: result of the battle (win or loose)
        :return: None


        """
        BattleResult.result = result
        BattleResult.monster = self.monster
        BattleResult.hero = self.battle_hero
        self.reequip()
        self.clear_battle_log()
        self.all_for_start()
        self.parent.current = "battle_result"
    pass

    @staticmethod
    def reequip():
        """Reequip main inventory after the ending of the battle.

        :return: None


        """
        main_inventory.del_potions_done()
        Battle.done_potions = []


class BattleResult(Screen):

    """Create anf run screen of showing results.

    """
    size_hint = (0.5, 0.5)
    result = 0
    hero = 0
    monster = 0

    class SeeResultButton(Button):
        pass

    def see_result(self):
        """Showing the result of battle.

        :return: None


        """
        n = self.SeeResultButton(text="See result")
        n.size_hint = 2, 2
        n.size = (self.width, self.height)
        self.add_widget(n)

    def result_output(self, text):
        """Show win or loose

        :param text: state of hero (win or loose)
        :return: None


        """
        self.ids.result_label.text = str(text)

    def win_result(self):
        """Run getting award for winning

        :return: None


        """
        self.hero = ReadHero.read_it()
        self.hero.gold += self.monster.gold
        self.hero.change_exp(self.monster.exp)
        ReadHero.save_it(self.hero)

    def result_go(self):
        """Result of battle showing manager

        :return:None
        """
        if self.result == "win":
            self.win_result()
        text = "Your result: \n   "+ str(self.result) + "\n"
        if self.result == "win":
            text += "Your loot: \n   " + str(self.monster.gold) + " coins\n   " + str(self.monster.exp) + " exp\n"
        self.result_output(text)

    pass


class Inventory(Screen):

    class ItemButton(Button):
        pass

    def equip_item(self, _id):
        """Run the equipping thing up.

        :param _id: id of thing
        :return: None


        """
        _id = int(_id)
        EquippingRunner.put_it_on(_id)

    def unequip_item(self, _id):
        """Run the unequipping the thing

        :param _id: id og thing
        :return: None


        """
        _id = int(_id)
        EquippingRunner.put_it_off(_id)
        self.show_equipment()

    def create_description(self, _name, _id):
        """Create the description of the obj for buing.

        :param _name: name of obj
        :param _id: id of obj
        :return: None


        """
        self.ids.description_label.text = str(_name)
        self.ids.description_label.name = str(_id)

    def show_equipment(self):
        """Show all equipment buttons on a screen

        :return: None


        """
        self.ids.here.clear_widgets()
        self.ids.description_label.text = ""
        self.ids.description_label.name = ""
        self.ids.show_equipment.state = "down"
        self.ids.show_artefacts.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_armour.state = "normal"
        self.ids.equip_button.text = "Unequip"
        items_in_shop = Battle.battle_inventory.get_potions()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)
        items_in_shop = Battle.battle_inventory.get_armors()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)
        items_in_shop = Battle.battle_inventory.get_artefacts()
        for i in items_in_shop:
            n = self.ItemButton(text=str(i.key))
            n.id = i.id
            self.ids.here.add_widget(n)

    def show_armour(self):
        """Show armor buttons

        :return: None


        """
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
        """ Show equipment buttons

        :return: None


        """
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
        """ Show potions buttons

        :return: None


        """
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
        """Clear all buttons

        :return:None


        """
        self.ids.here.clear_widgets()
    pass


class Shop(Screen):

    class ShopItemButton(Button):
        pass

    def amount_of_gold(self):
        """ Get money adventurer have

        :return: None


        """
        gold = str(ReadHero.read_it().gold)
        return gold

    def create_description(self, _name, _id):
        """Create description of thing

        :param _name: name of thing
        :param _id: id of thing
        :return: None


        """
        self.ids.description_label.text = str(_name)
        self.ids.description_label.name = str(_id)

    def buy_armor(self, _id):
        """Run buying armor

        :param _id: id of armor
        :return: None


        """
        Buying.buy_armor(int(_id))

    def buy_artefact(self, _id):
        """Run buying artefacts

        :param _id: id of artefact
        :return: None


        """
        Buying.buy_artefact(int(_id))

    def buy_potion(self, _id):
        """Run buying potion

        :param _id: id of potion
        :return: None


        """
        Buying.buy_potion(int(_id))

    def show_armour(self):
        """Show armors buttons

        :return: None


        """
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
        """Show artefacts buttons

        :return: None


        """
        self.ids.here.clear_widgets()
        self.ids.show_armour.state = "normal"
        self.ids.show_potions.state = "normal"
        self.ids.show_artefacts.state = "down"
        for i in Sellers.selling_artefacts:
            n = self.ShopItemButton(size=(125, 125), text=str(Sellers.selling_artefacts[i].key) + "\nCost: " + str(Sellers.selling_artefacts[i].cost))
            n.id = Sellers.selling_artefacts[i].id
            self.ids.here.add_widget(n)

    def show_potions(self):
        """Show potions buttons

        :return: None


        """
        self.ids.show_artefacts.state = "normal"
        self.ids.show_armour.state = "normal"
        self.ids.show_potions.state = "down"
        self.ids.here.clear_widgets()
        for i in Sellers.selling_potions:
            n = self.ShopItemButton(size=(125, 125), text=str(Sellers.selling_potions[i].key) + "\nCost: " + str(Sellers.selling_potions[i].cost))
            n.id = Sellers.selling_potions[i].id
            self.ids.here.add_widget(n)

    def clear_buttons(self):
        """Clear buttons

        :return: None


        """
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
    """The main app runner

    """
    def build(self):
        """Build screen

        :return: kivy file for building screen
        """
        return kv


if __name__ == '__main__':
    MyApp().run()

