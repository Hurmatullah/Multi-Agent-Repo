import time
import asyncio
from spade import agent, quit_spade
from spade.behaviour import OneShotBehaviour
from spade.message import Message

class AgentSendMessage(agent.Agent):
    class Mybehave(OneShotBehaviour):
        async def run(self):
            print("Agent behave is now running")
            msg = Message(to="saeed89@jabbers.one")
            msg.set_metadata("performative", "inform")
            msg.set_metadata("ontology", "myontology")
            msg.set_metadata("language", "OWL-S")
            msg.body = "Hello I am agent Karimi"

            await self.send(msg)
            print("Message is sent!")

            self.exit_code = "Job is finished"

            await self.agent.stop()
            print("Agent behavior is stopped")

    async def setup(self):
        print("Agent is now is setting up")
        self.b = self.Mybehave()
        self.add_behaviour(self.b)

AgentObject = AgentSendMessage("Karimi@deshalbfrei.org", "321456")
future = AgentObject.start()
future.result()

while AgentObject.is_alive():
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        AgentSendMessage.stop()
print("Agent process is finished!")