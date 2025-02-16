Mythological_Dictionary = {
    "La Llorona":"A ghostly figure in Mexican folklore, often depicted as a woman in white who mourns her drowned children. According to the legend, she wanders near bodies of water, weeping and calling out for her lost children. Her story is often used to warn children to stay away from water at night.",
    "Tiamat":"A primordial goddess of the sea, depicted as a dragon-like creature, who fought the god Marduk in the creation myth.",
    "Nian":"A mythical beast in Chinese folklore, said to emerge from the mountains to terrorize villages, especially during the Lunar New Year.",
    "Atalanta":"A famed hunter and warrior in Greek mythology, known for her speed and her roles in the hunt for the Calydonian Boar.",
    "Inanna":"The goddess of love, beauty, and war in Sumerian mythology, known for her journey to the underworld.",
    "Fenrir":"A monstrous wolf destined to fight and kill Odin during Ragnarok.",
    "Set":"The god of chaos, desert, and storms in ancient Egyptian mythology, often portrayed as an antagonist to other gods like Osiris.",
    "Arachne":"A talented mortal weaver who was transformed into a spider by Athena after challenging her in a weaving contest.",
    "Ganesha":"The elephant-headed god of wisdom, prosperity, and the remover of obstacles in Hinduism.",
    "Cerberus":"The three-headed dog guards the gates of the underworld, preventing souls from escaping.",
    "Echidna":"The mother of many famous monsters in Greek mythology, including Cerberus and the Hydra, often depicted as a half-woman, half-snake creature.",
    "Valkyrie":"Female warriors who serve Odin, choosing which warriors will die and bringing them to Valhalla.",
    "Amaterasu":"The sun goddess in Shinto mythology, and one of the most important deities in the Japanese pantheon.",
    "Mjolnir":"The magical hammer of Thor, capable of summoning thunder and lightning and never missing its target.",
    "Persephone":"Queen of the underworld and goddess of spring, abducted by Hades to rule by his side.",
    "Nuckelavee":"A terrifying, skinless horse-like demon from Orcadian mythology.",
    "Rusalka":"A water spirit or ghost of a young woman, often associated with lakes and rivers, known for luring men to their doom.",
    "Quetzalcoatl":"The feathered serpent god of wind, rain, and creation in Aztec mythology.",
    "Medusa":"A Gorgon, a monster with snakes for hair, whose gaze could turn people to stone.",
    "Yggdrasil":"The World Tree in Norse mythology, connecting all the nine realms of existence.",
    "Phoenix":"A mythical bird that regenerates by bursting into flames and rising again from its ashes, symbolizing rebirt and immortality.",
    "Banshee":"A wailing female spirit in Irish folklore, whose cries foretell the death of a family member.",
    "Hermes":"The messenger of the gods, god of travel, trade, and the thieves, often depected with winged sandals.",
    "Charybdis":"A monstrous sea creature that creates a deadly whirlpool, swallowing ships and sailors, associated with the myth of Odysseus.",
    "Zeus":"The king of the gods in Greek mythology, ruler of Mount Olympus, and god of thunder and lighting.",
    "Thor":"God of thunder, storms, and protection, known for wielding the hammer Mjolnir.",
    "Anansi":"A spider god and trickster figure in West African folklore, often depicted as a storyteller and wise figure.",
    "Hades":"God of the underworld, ruling over the souls of the dead and the riches of the earth.",
    "Kali":"The goddess of destruction and transformation, known for her fearsome appearance and her role in breaking down illusions.",
    "Odin":"The Allfather, ruler of the gods in Norse mythology, god of wisdom, war, and poetry."
}
while True:
    name = input("Search Mythological Terms:")
    print(Mythological_Dictionary.get(name, "Term is not on the list!"))