from discord import app_commands
import discord
from discord.ext.commands import Cog
from connection import DBConnection

class RoleCog(Cog):
    def init(self, bot):
        self.bot = bot
        self.db = DBConnection()
    #app command is the tree thing. used for creating role,
    @app_commands.command(name="create-role", description="Create a new role")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        if discord.utils.get(interaction.guild.roles, name=role_name):
            return await interaction.response.send_message(f"Role already exists", delete_after=4)
        role= await interaction.guild.create_role(name=role_name) 
        await interaction.response.send_message(f"Created a new role {role.mention}", delete_after=4)

    @app_commands.command(name="assign-role",description="Assign a role to a user")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def assign_role(self, interaction:discord.Interaction, member:discord.Member, role: discord.Role):
        await member.add_roles(role)
        #remove_roles(role) for removing it
        await interaction.response.send_message(f"Assigned {role.mention} to {member.mention}", delete_after=4)

async def setup(bot):
    await bot.add_cog(RoleCog(bot))