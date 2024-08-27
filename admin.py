import discord

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

client = discord.Client(intents=intents)

VOICE_CHANNEL_NAME = 'HDB-CTC-TT'
TEXT_CHANNEL_NAME = 'chat'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Tự động tham gia vào kênh thoại khi bot khởi động
    guild = discord.utils.get(client.guilds, name='Bang Thích')
    voice_channel = discord.utils.get(guild.voice_channels,
                                      name=VOICE_CHANNEL_NAME)
    if voice_channel:
        await voice_channel.connect()


@client.event
async def on_voice_state_update(member, before, after):
    # Log để kiểm tra sự kiện voice state update
    print(
        f'Voice state update: {member.display_name} - Before: {before.channel} / After: {after.channel}'
    )

    if after.channel and after.channel.name == VOICE_CHANNEL_NAME and before.channel != after.channel:
        text_channel = discord.utils.get(member.guild.text_channels,
                                         name=TEXT_CHANNEL_NAME)
        if text_channel:
            await text_channel.send(
                f'{member.display_name} vừa mới tham gia kênh thoại {VOICE_CHANNEL_NAME}'
            )


client.run(
    'MTI3ODAzOTI2ODExNTM1MzY0Mg.Gk-cs-.cobg6rcvPy4ePY1xN3d5I_Ou08bz038SLa_24I00')
