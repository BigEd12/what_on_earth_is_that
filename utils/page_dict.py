plant_dict = {
    'Daylilies': 'https://garden.org/plants/view/181473/Daylilies-Hemerocallis/',
    'Irises': 'https://garden.org/plants/view/181474/Irises-Iris/',
    'Roses': 'https://garden.org/plants/view/181506/Roses-Rosa/',
    'Sempervivum': 'https://garden.org/plants/view/186377/Sempervivum/',
    'Hostas': 'https://garden.org/plants/view/181510/Hostas-Hosta/',
    'Lilies': 'https://garden.org/plants/view/77555/Lilies-Lilium/',
    'Dahlias': 'https://garden.org/plants/view/76165/Dahlias-Dahlia/',
    'Peonies': 'https://garden.org/plants/view/530825/Peonies-Paeonia/',
    'Salvias': 'https://garden.org/plants/view/228296/Salvias-Salvia/',
    'Abelias': 'https://garden.org/plants/view/242735/Abelias-Vesalea/',
    'Abutilons': 'https://garden.org/plants/view/242733/Abutilons-Callianthe/',
    'Adeniums': 'https://garden.org/plants/view/242253/Adeniums-Adenium/',
    'Aeoniums': 'https://garden.org/plants/view/649201/Aeoniums-Aeonium/',
    'Agapanthus': 'https://garden.org/plants/view/75143/Lily-of-the-Nile-Agapanthus/',
    'Agaves': 'https://garden.org/plants/view/242254/Agaves-Agave/',
    'Aglaonemas': 'https://garden.org/plants/view/71544/Aglaonemas-Aglaonema/',
    'Air Plants': 'https://garden.org/plants/view/232959/Air-Plants-Tillandsia/',
    'Aloes': 'https://garden.org/plants/view/242252/Aloes-Aloe/',
    'Amaryllis': 'https://garden.org/plants/view/76980/Amaryllis/',
    'Amorphophallus': 'https://garden.org/plants/view/243338/Voodoo-Plant-Amorphophallus/',
    "Angel's Trumpets": 'https://garden.org/plants/view/236057/Angels-Trumpets-Brugmansia/',
    'Anise Hyssops': 'https://garden.org/plants/view/242700/Anise-Hyssops-Agastache/',
    'Anthuriums': 'https://garden.org/plants/view/538637/Anthuriums-Anthurium/',
    'Apples': 'https://garden.org/plants/view/86564/Apples-Malus/',
    'Apricots': 'https://garden.org/plants/view/114689/Apricots-Prunus-armeniaca/',
    'Arborvitaes': 'https://garden.org/plants/view/710373/Arborvitaes-Thuja/',
    'Arisaemas': 'https://garden.org/plants/view/528695/Arisaemas-Arisaema/',
    'Artichokes': 'https://garden.org/plants/view/87062/Artichokes-Cynara-scolymus/',
    'Arums': 'https://garden.org/plants/view/641388/Arums-Arum/',
    'Asparagus': 'https://garden.org/plants/view/86226/Asparagus-Asparagus-officinalis/',
    'Asters': 'https://garden.org/plants/view/232412/Asters-Aster/',
    'Astilbes': 'https://garden.org/plants/view/242590/Astilbes-Astilbe/',
    'Astragaluses': 'https://garden.org/plants/view/536504/Astragaluses-Astragalus/',
    "Baby's Breaths": 'https://garden.org/plants/view/126348/Babys-Breaths-Gypsophila-elegans/',
    'Bananas': 'https://garden.org/plants/view/533137/Bananas-Musa/',
    'Baptisias': 'https://garden.org/plants/view/536505/Baptisias-Baptisia/',
    'Barberries': 'https://garden.org/plants/view/240127/Barberries-Berberis/',
    'Basils': 'https://garden.org/plants/view/588177/Basils-Ocimum/',
    'Beans': 'https://garden.org/plants/view/86830/Beans-Phaseolus-vulgaris/',
    'Beautyberries': 'https://garden.org/plants/view/737439/Beautyberries-Callicarpa/',
    'Bee Balms': 'https://garden.org/plants/view/242696/Bee-Balms-Monarda/',
    'Beets': 'https://garden.org/plants/view/530731/Beets-Beta/',
    'Begonias': 'https://garden.org/plants/view/75518/Begonias-Begonia/',
    'Bellflowers': 'https://garden.org/plants/view/528041/Bellflowers-Campanula/',
    'Black Eyed Susans': 'https://garden.org/plants/view/78788/Black-Eyed-Susans-Rudbeckia/',
    'Blanket Flowers': 'https://garden.org/plants/view/76606/Blanket-Flowers-Gaillardia/',
    'Bleeding Hearts': 'https://garden.org/plants/view/528113/Bleeding-Hearts-Lamprocapnos/',
    'Blood Lilies': 'https://garden.org/plants/view/528285/Blood-Lilies-Scadoxus/',
    'Bluebeards': 'https://garden.org/plants/view/528040/Bluebeards-Caryopteris/',
    'Bluestem Grasses': 'https://garden.org/plants/view/528284/Bluestem-Grasses-Andropogon/',
    'Bougainvilleas': 'https://garden.org/plants/view/75569/Bougainvilleas-Bougainvillea/',
    'Brassicas': 'https://garden.org/plants/view/229759/Brassicas-Brassica/',
    'Butterfly Bushes': 'https://garden.org/plants/view/649002/Butterfly-Bushes-Buddleja/',
    'Butterworts': 'https://garden.org/plants/view/809714/Butterworts-Pinguicula/',
    'Caladiums': 'https://garden.org/plants/view/527355/Caladiums-Caladium/',
    'Calibrachoas': 'https://garden.org/plants/view/75655/Calibrachoas-Calibrachoa/',
    'Callas': 'https://garden.org/plants/view/233380/Callas-Zantedeschia/',
    'Camellias': 'https://garden.org/plants/view/75683/Camellias-Camellia/',
    'Cannas': 'https://garden.org/plants/view/75726/Cannas-Canna/',
    'Cantaloupes': 'https://garden.org/plants/view/87175/Cantaloupes-Cucumis-melo/',
    'Cape Lilies': 'https://garden.org/plants/view/527558/Cape-Lilies-Nerine/',
    'Cape Primroses': 'https://garden.org/plants/view/79113/Cape-Primroses-Streptocarpus/',
    'Carrots': 'https://garden.org/plants/view/386216/Carrots-Daucus-carota-var-sativus/',
    'Castor Beans': 'https://garden.org/plants/view/78747/Castor-Beans-Ricinus-communis/',
    'Catmints': 'https://garden.org/plants/view/242695/Catmints-Nepeta/',
    'Celeries': 'https://garden.org/plants/view/737487/Celeries-Apium/',
    'Chickweed': 'https://garden.org/plants/view/528417/Chickweed-Cerastium/',
    'Chives': 'https://garden.org/plants/view/75204/Chives-Allium-schoenoprasum/',
    'Chlorophytums': 'https://garden.org/plants/view/527545/Chlorophytums-Chlorophytum/',
    'Chollas': 'https://garden.org/plants/view/232894/Chollas-Cylindropuntia/',
    'Cilantros': 'https://garden.org/plants/view/86729/Cilantros-Coriandrum-sativum/',
    'Citrus Fruits': 'https://garden.org/plants/view/242635/Citrus-Fruits-Citrus/',
    'Clematis': 'https://garden.org/plants/view/181489/Clematis/',
    'Clivias': 'https://garden.org/plants/view/242628/Clivias-Clivia/',
    'Colchicums': 'https://garden.org/plants/view/75960/Colchicums-Colchicum/',
    'Coleus': 'https://garden.org/plants/view/79005/Coleus-Coleus-scutellarioides/',
    'Columbines': 'https://garden.org/plants/view/75302/Columbines-Aquilegia/',
    'Coneflowers': 'https://garden.org/plants/view/185972/Coneflowers-Echinacea/',
    'Consolidas': 'https://garden.org/plants/view/646103/Consolidas-Consolida/',
    'Coral Bells': 'https://garden.org/plants/view/232967/Coral-Bells-Heuchera/',
    'Corn': 'https://garden.org/plants/view/695646/Corn-Zea/',
    'Cosmos': 'https://garden.org/plants/view/528112/Cosmos/',
    'Crassulas': 'https://garden.org/plants/view/242255/Crassulas-Crassula/',
    'Crepe Myrtles': 'https://garden.org/plants/view/181507/Crepe-Myrtles-Lagerstroemia/',
    'Crinums': 'https://garden.org/plants/view/76120/Crinums-Crinum/',
    'Crocosmias': 'https://garden.org/plants/view/242597/Crocosmias-Crocosmia/',
    'Crocus': 'https://garden.org/plants/view/242588/Crocus/',
    'Crotons': 'https://garden.org/plants/view/240116/Crotons-Codiaeum/',
    'Cucumbers': 'https://garden.org/plants/view/546944/Cucumbers-Cucumis-sativus/',
    'Culinary Sages': 'https://garden.org/plants/view/4663/Culinary-Sages-Salvia-officinalis/',
    'Currants And Gooseberries': 'https://garden.org/plants/view/737497/Currants-and-Gooseberries-Ribes/',
    'Dead Nettles': 'https://garden.org/plants/view/242648/Dead-Nettles-Lamium/',
    'Delphiniums': 'https://garden.org/plants/view/76186/Delphiniums-Delphinium/',
    'Dianthus': 'https://garden.org/plants/view/76204/Dianthus/',
    'Dieffenbachias': 'https://garden.org/plants/view/645466/Dieffenbachias-Dieffenbachia/',
    'Dills': 'https://garden.org/plants/view/75274/Dills-Anethum-graveolens/',
    'Dogwoods': 'https://garden.org/plants/view/527547/Dogwoods-Cornus/',
    'Dracontiums': 'https://garden.org/plants/view/645122/Dracontiums-Dracontium/',
    'Dudleyas': 'https://garden.org/plants/view/242249/Dudleyas-Dudleya/',
    'Echeverias': 'https://garden.org/plants/view/117125/Echeverias-Echeveria/',
    'Eggplants': 'https://garden.org/plants/view/87688/Eggplants-Solanum-melongena/',
    'Elephant Ears (Alocasia)': 'https://garden.org/plants/view/75214/Elephant-Ears-Alocasia-Alocasia/',
    'Elephant Ears (Colocasia)': 'https://garden.org/plants/view/242621/Elephant-Ears-Colocasia-Colocasia/',
    'Elephant Ears (Xanthosoma)': 'https://garden.org/plants/view/537490/Elephant-Ears-Xanthosoma-Xanthosoma/',
    'Epiphyllum': 'https://garden.org/plants/view/589130/Epiphyllum/',
    'Erodiums': 'https://garden.org/plants/view/240734/Erodiums-Erodium/',
    'Erythroniums': 'https://garden.org/plants/view/536508/Erythroniums-Erythronium/',
    'Eupatoriums': 'https://garden.org/plants/view/536507/Eupatoriums-Eupatorium/',
    'Euphorbias': 'https://garden.org/plants/view/242586/Euphorbias-Euphorbia/',
    'False Bananas': 'https://garden.org/plants/view/533136/False-Bananas-Ensete/',
    'Figs': 'https://garden.org/plants/view/76528/Figs-Ficus-carica/',
    'Foamflowers': 'https://garden.org/plants/view/229091/Foamflowers-Tiarella/',
    'Foamy Bells': 'https://garden.org/plants/view/232966/Foamy-Bells-XHeucherella/',
    'Foxgloves': 'https://garden.org/plants/view/528115/Foxgloves-Digitalis/',
    'Freesias': 'https://garden.org/plants/view/76597/Freesias-Freesia/',
    'Fritillarias': 'https://garden.org/plants/view/656551/Fritillarias-Fritillaria/',
    'Fuchsias': 'https://garden.org/plants/view/76601/Fuchsias-Fuchsia/',
    'Garden Nasturtiums': 'https://garden.org/plants/view/185903/Garden-Nasturtiums-Tropaeolum-majus/',
    'Gardenias': 'https://garden.org/plants/view/612276/Gardenias-Gardenia/',
    'Garlic': 'https://garden.org/plants/view/75203/Garlic-Allium-sativum/',
    'Gayfeathers': 'https://garden.org/plants/view/536509/Gayfeathers-Liatris/',
    'Geraniums': 'https://garden.org/plants/view/233659/Geraniums-Geranium/',
    'Ginger Lilies': 'https://garden.org/plants/view/659229/Ginger-Lilies-Hedychium/',
    'Gingers': 'https://garden.org/plants/view/659230/Gingers-Zingiber/',
    'Gladiolus': 'https://garden.org/plants/view/76715/Gladiola-Gladiolus/',
    'Goldenrods': 'https://garden.org/plants/view/527712/Goldenrods-Solidago/',
    'Gourds, Squashes And Pumpkins': 'https://garden.org/plants/view/242703/Gourds-Squashes-and-Pumpkins-Cucurbita/',
    'Grape Hyacinths': 'https://garden.org/plants/view/236410/Grape-Hyacinths-Muscari/',
    'Grapes': 'https://garden.org/plants/view/706088/Grapes-Vitis/',
    'Heavenly Bamboos': 'https://garden.org/plants/view/181462/Heavenly-Bamboos-Nandina-domestica/',
    'Hellebores': 'https://garden.org/plants/view/240735/Hellebores-Helleborus/',
    'Hibiscus': 'https://garden.org/plants/view/242680/Hibiscus/',
    'Homalomenas': 'https://garden.org/plants/view/645477/Homalomenas-Homalomena/',
    'Honeysuckles': 'https://garden.org/plants/view/527546/Honeysuckles-Lonicera/',
    'Hoyas': 'https://garden.org/plants/view/228342/Hoyas-Hoya/',
    'Hyacinths': 'https://garden.org/plants/view/527149/Hyacinths-Hyacinthus/',
    'Hydrangeas': 'https://garden.org/plants/view/232782/Hydrangeas-Hydrangea/',
    'Ilex': 'https://garden.org/plants/view/546842/Ilex/',
    'Joe Pye Weed': 'https://garden.org/plants/view/528424/Joe-Pye-Weed-Eutrochium/',
    'Jujubes': 'https://garden.org/plants/view/109204/Jujubes-Ziziphus-jujuba/',
    'Kalanchoes': 'https://garden.org/plants/view/242256/Kalanchoes-Kalanchoe/',
}