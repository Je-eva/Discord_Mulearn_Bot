import discord
from discord.ext import commands
from tasksdb import TaskDB

class Rank(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.db=TaskDB()
        
    @discord.app_commands.command(name="get-karma")
    async def get_karma(self,interaction,user:discord.Member=None):
        user = user or interaction.user
        karma = self.db.get_user_karma(user.name)
        embed = discord.Embed(title="Total Karma",description=karma[0],color=discord.Color.random())
        await interaction.response.send_message(embed=embed)
        
    
async def setup(bot):
    await bot.add_cog(Rank(bot))