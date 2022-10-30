from spade import agent, quit_spade

class CreatingNewAgent(agent.Agent):
    async def setup(self):
        print("Hello dear Mr.Hurmat created me with this id {}".format(str(self.jid)))

AgentObject = CreatingNewAgent("Karimi@deshalbfrei.org", "321456")
result1 = AgentObject.start()
result1.result()


AgentObject.stop()
quit_spade()