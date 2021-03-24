import discord

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
            embed.add_field(name='구매자 : ', value=message.author, inline=False)
            embed.add_field(name='후기 내용', value=message.content, inline=False)
            embed.set_footer(text=f'후기작성은 <@{message.author.id}> !후기작성 [후기]를 입력해주세요!')
            await client.get_channel(809222874253492245).send(f"`{message.author.name}({message.author.id})`", embed=embed)

    if message.content.startswith('>후기작성'):
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(f"**{message.author.name}** 님의 후기 : {msg}")
            await message.channel.send(f'`{message.mentions[0]}`님 후기를 보냈어요')
        else:
            return

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
