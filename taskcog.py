import discord
from discord.ext import commands
from tasksdb import TaskDB
class TaskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db=TaskDB()
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith("#t1"):
            self.db.task_insertion(message)
            
            
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.emoji.name =="😭":
            self.db.award_karma(payload.message_id,payload.user_id)
            
    @commands.Cog.listener()
    async def on_raw_message_delete(self,payload):
        self.db.delete_message(payload.message_id)
        
async def setup(bot):
    await bot.add_cog(TaskCog(bot))