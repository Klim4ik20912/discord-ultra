import disnake
from disnake.ext import commands

class PrivateVoiceChannels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None and after.channel.id == 1089655352674500759:
            category = after.channel.category
            overwrites = {
                member.guild.default_role: disnake.PermissionOverwrite(read_messages=False),
                member: disnake.PermissionOverwrite(read_messages=True)
            }
            voice_channel = await member.guild.create_voice_channel(
                f'Приватный канал {member.name}', overwrites=overwrites, category=category
            )
            await member.move_to(voice_channel)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if not payload.member.bot:
            channel = self.bot.get_channel(payload.channel_id)
            if isinstance(channel, disnake.VoiceChannel):
                if payload.emoji.name == '🔒':
                    await channel.set_permissions(payload.member.guild.default_role, read_messages=False)
                elif payload.emoji.name == '🔓':
                    await channel.set_permissions(payload.member.guild.default_role, read_messages=True)
                elif payload.emoji.name == '✏️':
                    await channel.edit(name=f'Новое название {payload.member.name}')
                else:
                    member = payload.member.guild.get_member(payload.user_id)
                    if member is not None:
                        await channel.set_permissions(member, read_messages=True)

def setup(bot):
    bot.add_cog(PrivateVoiceChannels(bot))
