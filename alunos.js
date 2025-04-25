const prompt = require('prompt-sync')();

let alunos = [];
function menu() {
    console.log('MENU');
    console.log(' 1. adicionar aluno(a)\n 2. listar alunos\n 3. buscar aluno(a)\n 4. editar aluno(a)\n 5. sair');
    let escolha = prompt('Escolha uma opção: ');
    return escolha;
};

function add_alunos (id) {
    let nome = prompt('Nome do aluno(a): ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = parseFloat(prompt(`Nota ${i} do aluno(a): `));
        notas.push(nota);
    }

    console.log(`Aluno(a) ${nome} adicionado com sucesso!`)
    alunos.push({id: id, nome: nome, notas: notas = notas, media: (notas.reduce((acumulador, atual) => acumulador + atual, 0) / 3).toFixed(2)});
    return id += 1;
};

function listar_alunos () {
    for (let aluno of alunos) {
        console.log(`Aluno(a): ${aluno['nome']}, ID: ${aluno['id']}`);
        let quantidade = aluno['notas'].length 
        for (let i = 0; i < quantidade; i++) {
            console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
        }
        console.log(`Média: ${aluno['media']}`);
        console.log();
    }
};

function buscar_aluno () {
    let buscar_nome = prompt('Nome do aluno(a) que deseja procurar: ');
    let verificacao = false;
    for (let aluno of alunos) {
        if (buscar_nome.toLowerCase() == aluno['nome'].toLowerCase()) {
            console.log(`Aluno(a): ${aluno['nome']}`);
            verificacao = true;
            let quantidade = aluno['notas'].length 
            for (let i = 0; i < quantidade; i++) {
                console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
            }
        }
    }
    if (verificacao == false) {
        console.log(`Aluno(a) ${buscar_nome} não encontrado!`);
    }
};

function editar_aluno () {
    let modificar = prompt('O que deseja editar [1 -> nome do aluno(a), 2 -> notas do aluno(a)] ');
    console.log('Alunos cadastrados');
    for (let aluno of alunos) {
        console.log(`Nome: ${aluno['nome']}, notas: ${aluno['nota']}`);
    }
    if (modificar == '1') { 
        let escolha_nome = prompt('Digite o nome do aluno: '); 
        let verificacao = false;
        for (let aluno of alunos) {
            if (escolha_nome.toLocaleLowerCase() == aluno['nome'].toLocaleLowerCase()) {
                aluno['nome'] = escolha_nome;
                verificacao = true;
                console.log('Mudança feita!');
                console.log(`${aluno['nome']} -> ${escolha_nome}`)
            }
        }
        if (verificacao == false) {
            console.log(`Aluno ${escolha_nome} não encontrado!`)
        }
    }
}

let id = 1;

while (true) {
    escolha = menu();
    if (escolha == '1') {
        add_alunos(id);
    }
    else if (escolha == '2') {
        listar_alunos();
    }
    else if (escolha == '3') {
        buscar_aluno();
    }
    else if (escolha == '4') {
        editar_aluno();
    }
    else if (escolha == '5') {
        console.log('Fim do programa!');
        break;
    }
    else {
        console.log('Opção inválida!');
    }
}