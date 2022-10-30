import time
import asyncio
from spade import agent, quit_spade
from spade.behaviour import CyclicBehaviour

class AgentWithBehavior(agent.Agent):
    class Mybehav(CyclicBehaviour):
        async def on_start(self):
            print("Agent process is started")
            self.counter = 0

        async def run(self):
            print("Agent now is running".format(self.counter))
            self.counter += 1
            await asyncio.sleep(1)

    #Creating setup for agents
    async def setup(self):
        print("Agent is starting with behaviors")
        p = self.Mybehav()
        self.add_behaviour(p)

Agent1 = AgentWithBehavior("Karimi@deshalbfrei.org", "321456")
future = Agent1.start()
future.result()

Agent1.stop()
quit_spade()

