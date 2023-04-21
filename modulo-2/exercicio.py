
# -1 LISTAS
top_10_filmes = set(['batima', 'doutor estranho no multiverso da loucura', 'thor: amor e trovao', 'top Gun: meverick', 'pantera negra: wakanda para sempre', 'o homen do norte', 'agente oculto', 'tudo em todo lugar ao mesmo tempo', 'a morte do nilo', 'x-a marca da morte'])

# print(top_10_filmes)

# -1.2 simular movimrntacao sando metodo pop e unset
# posicao = top_10_filmes.index("batima")
# print(posicao)
# # adicionando no lista com metodo unsert()
# top_10_filmes.insert(0, "a morte do nilo")
# print(top_10_filmes)
# # removendo elemento usando usando metodo pop()
# top_10_filmes.pop(0)
# print(top_10_filmes)

# -2 Conjuntos
# mylist = list(top_10_filmes)
# print(type(mylist))
# print(top_10_filmes)

# -3 dicionarios
filmes = {
     'Batman':{
          'nome': 'Batman',
          'ano': 2022,
          'sinopse': ' Batman de 2022 traz o herói na busca pelo Charada (Paul Dano), criminoso que vem dizimando figuras notáveis de Gotham e que parece ter uma questão particular para resolver com o vigilante.',
     },
     'Doutor Estranho no Multiverso da Loucura':{
          'nome': 'Doutor Estranho no Multiverso da Loucura',
          'ano': 2022,
          'sinopse': 'Doutor Estranho no Multiverso da Loucura, apos derrotar Dormammu e enfrentar Thanos nos eventos de Vingadores: Ultimato, o Mago Supremo, Stephen Strange (Benedict Cumberbatch), e seu parceiro Wong (Benedict Wong), continuam suas pesquisas sobre a Joia do Tempo.',
     },
     'Thor: Amor e Trovão':{
          'nome': 'Thor: Amor e Trovão',
          'ano': 2022,
          'sinopse': 'Ansiando por um propósito, Thor retorna à Nova Asgard e sua aposentadoria é interrompida por um assassino galáctico conhecido como Gorr, o Carniceiro de Deus, que busca a extinção dos deuses.',
     },
      'Top Gun: Maverick':{
          'nome': 'Top Gun: Maverick',
          'ano': 2022,
          'sinopse': 'Depois de mais de trinta anos de serviço como um dos principais aviadores da Força Aeronaval, Pete Mitchell (Tom Cruise), mais conhecido como Maverick, está onde pertence.',
     },
      'Pantera Negra: Wakanda Para Sempre':{
          'nome': 'Pantera Negra: Wakanda Para Sempre',
          'ano': 2022,
          'sinopse': "Após a morte do ator de T'Challa (Chadwick Boseman) o foco de Wakanda Para Sempre são os personagens em volta do Pantera Negra. Rainha Ramonda (Angela Bassett), Shuri (Letitia Wright), M'Baku (Winston Duke), Okoye (Danai Gurira) e as Dora Milage lutam para proteger a nação fragilizada de outros países após a morte de T'Challa",
     },
      'O Homem do Norte':{
          'nome': 'O Homem do Norte',
          'ano': 2022,
          'sinopse': 'O Homem do Norte segue uma história de vingança e loucura de um príncipe. Se passando no ápice da Landnámsöld, no ano de 914, o príncipe Amleth (Alexander Skarsgård) está prestes atingir maioridade e ocupar o espaço de seu pai, o rei Horvendill (Ethan Hawke), que acaba sendo brutalmente assassinado.',
     },
      'Agente Oculto':{
          'nome': 'Agente Oculto',
          'ano': 2022,
          'sinopse': 'O filme Agente Oculto acompanha a história de Gentry, um dos melhores e mais letais mercenários da CIA – que ninguém sabe a real identidade. Ele embarca em uma missão pela Europa para resgatar seu contratante, Sir Donald Fitzroy, e sua família, de Lloyd, membro de uma gigantesca corporação francesa e ex-oficial da CIA.',
     },
      'Tudo em Todo Lugar ao Mesmo Tempo':{
          'nome': 'Tudo em Todo Lugar ao Mesmo Tempo',
          'ano': 2022,
          'sinopse': 'Em Tudo em Todo Lugar ao Mesmo Tempo, acompanhamos uma sobrecarregada imigrante chinesa, Evelyn Wang (Michelle Yeoh) que com sua lavanderia à beira do fracasso e seu casamento com o marido covarde em ruínas, ela luta para lidar com tudo, incluindo um relacionamento ruim com seu pai crítico e sua filha (Stephanie Hsu).',
     },
      'A Morte no Nilo':{
          'nome': 'A Morte no Nilo',
          'ano': 2022,
          'sinopse': 'Em Morte no Nilo, durante sua viagem de lua de mel pelo rio Nilo, o casal Linnet Ridgeway (Gal Gadot) e Simon Doyle (Armie Hammer), convidaram os entes mais queridos para embarcar no barco Karvak e celebrar a união do casal.',
     },
      'X – A Marca da Morte':{
          'nome': 'X – A Marca da Morte',
          'ano': 2022,
          'sinopse': 'Em X: A Marca da Morte, novo filme de terror slasher do diretor Ti West, acompanha um grupo de cineastas pornográficos em sua gravação de um novo longa. Em 1979, Maxine, uma atriz pornô, Wayne seu namorado e produtor e mais um grupo de atores e pessoas vão para o Texas em uma fazenda, propriedade de Howard e Pearl, um casal idoso, para gravar o novo filme pornográfico The Farmer’s Daughters.',
     }
}

print(filmes)