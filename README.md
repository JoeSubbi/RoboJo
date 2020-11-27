# RoboJo - Discord Bot

RoboJo is equpied with passive behaviour and command driven behaviour. The passive behaviour detects patterns in what people say on the discord chat, whilst the command behaviour is triggered when a command is detected (prefixed with '`!`').

## Passive Behaviour
> (This part is quite dumb)

### `Thanks for the upvote kind stranger`
When a media post is sent to the chat such as a gif or image, RoboJo will react to the post with an upvote and a downvote arrow. This allows other members of your server to add an upvote or downvote to the this post.

This functionality does not extend to links to embedded media e.g Giphy or YouTube

### `Happy Birthday!`
If anyone types "Happy Birthday" (or "Happy Birfday" don't ask me why) RoboJo will also respond with its own congratulations into the chat.

### `Shaking My Head...`
type in "smh" and here is your free emote to show your friends just how dissapointed you truly are.  
<sub>yes thats me IRL Joe...

### `69 and 420...?`
Whenever someone types a 69 or 420 in the chat RoboJo will reply with a "***Nice!*** ".  
The bot also detects when an emote ID or a gif/ID has either number in it so it may respond seemingly at random. I find this quite intresting but I will probably remove this unplanned feature in the future.



## Commands
### `!help`
This provides the standard help message listing information about all other commands. Type in !help \<command> to find more detail on that specific command

### `!pick`
Can't decide on something?  !pick \<things> will return a random thing.
When `!pick` is followed by a series of space seperated arguments, it will output one of these arguments at random")  
Example:  
> If I am playing games with my friends and we can't choose between Halo Titanfall 2 and Sea of Thieves I can simply type
    `!pick Halo Tf2 SoT` 
    and RoboJo could return: `Halo`

<!--
#Features to be added:

### `!upvote`
Type this into the chat and the specific channel and server id will be saved to a local file. This is then read by RoboJo noting that this channel in this server is to be recognised when utalising the upvote-downvote-reaction feature. This will be turned on by default to all channels

if followed by -all the feature will be enabled across the entire server (default) by removing the server ID from local file

### `!downvote`
Type this into a speific channel and the server id will be noted as not using the upvote-downvote-reaction feature on this specific channel of the server.

If followed by the argument -all the feature will be disabled for the entire server.

 -->