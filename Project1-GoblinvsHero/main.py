import time
import random
class character():
    defaulthealthhero=100
    defaulthealthgoblin=100
    # defaulthit=20
    token=True
    # okay lets keep the goblin as npc
    def action(self):
        if(self.token==True):
            print("-----------Hero's turn----------------")
            self.token=False
            choice=int(input("Type Your Attack\n 1 to Atttack(-20HP)\n 2 to HeavyAtttack(-40HP)\n 3 to Do Nothing"))
            if choice==1:
                print("hero has Performed Attack on the Goblin")
                print("Health of the goblin is depleted by 20HP")
                self.defaulthealthgoblin=self.defaulthealthgoblin-20
                time.sleep(2)
                print(f"Current Health of the Goblin is {self.defaulthealthgoblin}")
            elif choice==2:
                print("hero has Performed Heavy Attack on the Goblin")
                print("Health of the goblin is depleted by 40HP")
                self.defaulthealthgoblin=self.defaulthealthgoblin-40
                time.sleep(2)
                print(f"Current Health of the Goblin is {self.defaulthealthgoblin}")
            else:
                print("hero has Performed Nothing on the Goblin")
                print("Health of the goblin is depleted by 0HP")
                time.sleep(2)
                print(f"Current Health of the Goblin is {self.defaulthealthgoblin}")
        else:
            print("-----------Goblin's turn----------------")
            self.token=True
            print(f"HERO HEALTH: {self.defaulthealthhero}")
            print(f"Goblin HEALTH: {self.defaulthealthgoblin}")
            damage=random.randint(10,30)
            print("The Goblin is pllotting a attack")
            time.sleep(2)
            self.defaulthealthhero=self.defaulthealthhero-damage
            print("The Goblin bite the Hero Hand ....")
            time.sleep(2)
            print(f"-{damage}HP")
            time.sleep(2)
            print(f"The Current HP of yours is {self.defaulthealthhero}")


firstrun=character()
while firstrun.defaulthealthhero>0 and firstrun.defaulthealthgoblin>0:
   firstrun.action()






    