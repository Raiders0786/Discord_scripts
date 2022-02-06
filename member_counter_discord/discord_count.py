
import discum
from decouple import config

# Configure your Authentication bearer Token .
my_secret=config('TOKEN')
bot= discum.Client(token=my_secret)

def close_after_fetching(guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched))
        bot.gateway.removeCommand({'function':close_after_fetching,'guild_id':guild_id})
        bot.gateway.close()

def get_members(guild_id,channel_id):
    bot.gateway.fetchMembers(guild_id,channel_id,keep="all",wait=1)
    bot.gateway.command({'function':close_after_fetching,'guild_id':guild_id})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members("883268018875023390","883268018875023392")

membersList = []
for memberId in members:
    membersList.append(memberId)
    print(memberId)

f = open('users.txt',"w")
for elements in membersList:
    f.write(elements + '\n')
f.close()

with open("users.txt","r") as f:
    print("Total members in the Server :",len(f.readlines()))