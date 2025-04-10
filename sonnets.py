uncleaned_sonnets = {5: """Those hours that with gentle work did frame
The lovely gaze where every eye doth dwell
Will play the tyrants to the very same
And that unfair which fairly doth excel;
For never-resting time leads summer on
To hideous winter and confounds him there,
Sap checked with frost and lusty leaves quite gone,
Beauty o’er-snowed and bareness everywhere.
Then, were not summer’s distillation left
A liquid prisoner pent in walls of glass,
Beauty’s effect with beauty were bereft,
Nor it nor no remembrance what it was.
But flowers distilled, though they with winter meet,
Leese but their show; their substance still lives sweet.""", 
            9: """Is it for fear to wet a widow’s eye
That thou consum’st thyself in single life?
Ah, if thou issueless shalt hap to die,
The world will wail thee like a makeless wife;
The world will be thy widow and still weep
That thou no form of thee hast left behind,
When every private widow well may keep,
By children’s eyes, her husband’s shape in mind.
Look what an unthrift in the world doth spend
Shifts but his place, for still the world enjoys it;
But beauty’s waste hath in the world an end,
And, kept unused, the user so destroys it.
No love toward others in that bosom sits
That on himself such murd’rous shame commits.""",
           12: """When I do count the clock that tells the time
And see the brave day sunk in hideous night,
When I behold the violet past prime
And sable curls all silvered o’er with white;
When lofty trees I see barren of leaves,
Which erst from heat did canopy the herd,
And summer’s green all girded up in sheaves
Borne on the bier with white and bristly beard;
Then of thy beauty do I question make
That thou among the wastes of time must go,
Since sweets and beauties do themselves forsake
And die as fast as they see others grow;
And nothing ’gainst Time’s scythe can make defense
Save breed, to brave him when he takes thee hence.""",
           51: """Thus can my love excuse the slow offense
Of my dull bearer when from thee I speed:
From where thou art, why should I haste me thence?
Till I return, of posting is no need.
O, what excuse will my poor beast then find
When swift extremity can seem but slow?
Then should I spur, though mounted on the wind;
In wingèd speed no motion shall I know.
Then can no horse with my desire keep pace;
Therefore desire, of perfect’st love being made,
Shall neigh no dull flesh in his fiery race.
But love for love thus shall excuse my jade:
“Since from thee going he went willful slow,
Towards thee I’ll run, and give him leave to go.”""",
           54: """O, how much more doth beauty beauteous seem
By that sweet ornament which truth doth give.
The rose looks fair, but fairer we it deem
For that sweet odor which doth in it live.
The canker blooms have full as deep a dye
As the perfumèd tincture of the roses,
Hang on such thorns, and play as wantonly
When summer’s breath their maskèd buds discloses;
But, for their virtue only is their show,
They live unwooed and unrespected fade,
Die to themselves. Sweet roses do not so;
Of their sweet deaths are sweetest odors made.
And so of you, beauteous and lovely youth,
When that shall vade, by verse distils your truth.""",
           65: """ince brass, nor stone, nor earth, nor boundless sea
But sad mortality o’ersways their power,
How with this rage shall beauty hold a plea,
Whose action is no stronger than a flower?
O, how shall summer’s honey breath hold out
Against the wrackful siege of batt’ring days,
When rocks impregnable are not so stout
Nor gates of steel so strong, but Time decays?
O, fearful meditation! Where, alack,
Shall Time’s best jewel from Time’s chest lie hid?
Or what strong hand can hold his swift foot back,
Or who his spoil of beauty can forbid?
O, none, unless this miracle have might,
That in black ink my love may still shine bright.""",
           111: """O, for my sake do you with Fortune chide,
The guilty goddess of my harmful deeds,
That did not better for my life provide
Than public means which public manners breeds.
Thence comes it that my name receives a brand;
And almost thence my nature is subdued
To what it works in, like the dyer’s hand.
Pity me, then, and wish I were renewed,
Whilst, like a willing patient, I will drink
Potions of eisel ’gainst my strong infection;
No bitterness that I will bitter think,
Nor double penance, to correct correction.
Pity me, then, dear friend, and I assure ye
Even that your pity is enough to cure me.""",
           128: """How oft, when thou, my music, music play’st
Upon that blessèd wood whose motion sounds
With thy sweet fingers when thou gently sway’st
The wiry concord that mine ear confounds,
Do I envy those jacks that nimble leap
To kiss the tender inward of thy hand,
Whilst my poor lips, which should that harvest reap,
At the wood’s boldness by thee blushing stand.
To be so tickled they would change their state
And situation with those dancing chips,
O’er whom thy fingers walk with gentle gait,
Making dead wood more blest than living lips.
Since saucy jacks so happy are in this,
Give them thy fingers, me thy lips to kiss.""",
           130: """My mistress’ eyes are nothing like the sun;
Coral is far more red than her lips’ red;
If snow be white, why then her breasts are dun;
If hairs be wires, black wires grow on her head.
I have seen roses damasked, red and white,
But no such roses see I in her cheeks;
And in some perfumes is there more delight
Than in the breath that from my mistress reeks.
I love to hear her speak, yet well I know
That music hath a far more pleasing sound.
I grant I never saw a goddess go;
My mistress, when she walks, treads on the ground.
 And yet, by heaven, I think my love as rare
 As any she belied with false compare.""",
           153: """Cupid laid by his brand and fell asleep.
A maid of Dian’s this advantage found,
And his love-kindling fire did quickly steep
In a cold valley-fountain of that ground,
Which borrowed from this holy fire of Love
A dateless lively heat, still to endure,
And grew a seething bath which yet men prove
Against strange maladies a sovereign cure.
But at my mistress’ eye Love’s brand new fired,
The boy for trial needs would touch my breast;
I, sick withal, the help of bath desired
And thither hied, a sad distempered guest,
 But found no cure. The bath for my help lies
 Where Cupid got new fire—my mistress’ eyes.""",
           154: """The little love-god, lying once asleep,
Laid by his side his heart-inflaming brand,
Whilst many nymphs that vowed chaste life to keep
Came tripping by; but in her maiden hand
The fairest votary took up that fire,
Which many legions of true hearts had warmed;
And so the general of hot desire
Was, sleeping, by a virgin hand disarmed.
This brand she quenchèd in a cool well by,
Which from Love’s fire took heat perpetual,
Growing a bath and healthful remedy
For men diseased; but I, my mistress’ thrall,
 Came there for cure, and this by that I prove:
 Love’s fire heats water; water cools not love."""}

def remove_punctuation(text):
    for punctuation in ',.’?;:"-':
        text = text.replace(punctuation, "")
    return text

sonnets = {}
for sonnet_num in uncleaned_sonnets:
    sonnet = uncleaned_sonnets[sonnet_num]
    cleaned_sonnet = remove_punctuation(sonnet.lower())
    sonnets[sonnet_num] = cleaned_sonnet
