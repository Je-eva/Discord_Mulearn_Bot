from discord import app_commands
import discord
from discord.ext.commands import Cog

class HelpCog(Cog):    
    def init(self, bot):
        self.bot = bot
    @app_commands.command(name="help", description="To help u ahead")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def help(self,interaction):
        help_message = " use /create-role to createa aa role  \n use /asign-role to assign a role"
        await interaction.response.send_message(help_message)
        
async def setup(bot):
    await bot.add_cog(HelpCog(bot))