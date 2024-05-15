from opsdroid.skill import Skill
from opsdroid.matchers import match_event
from opsdroid.events import UserInvite, JoinRoom

class AcceptInv(Skill):
    @match_event(UserInvite)
    async def user_invite(self, invite):
        print('\n----User invite----\n')
        print(f"user invite ---> {invite}")
        if isinstance( invite, UserInvite):
            await invite.respond(JoinRoom())


