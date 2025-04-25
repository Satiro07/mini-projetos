const prompt = require('prompt-sync')();

let alunos = [];
function menu() {
    console.log('MENU');
    console.log(' 1. adicionar aluno\n 2. listar alunos\n 3. buscar aluno\n 4. sair');
    let escolha = prompt('Escolha uma opção: ');
    return escolha;
};

function add_alunos () {
    let nome = prompt('Nome do aluno: ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = parseFloat(prompt(`Nota ${i} do aluno: `));
        notas.push(nota);
    }
    console.log(`Aluno ${nome} adicionado com sucesso!`)
    alunos.push({nome: nome, notas: notas});
};

function listar_alunos () {
    for (let aluno of alunos) {
        console.log(`Aluno: ${aluno['nome']}`);
        let quantidade = aluno['notas'].length 
        for (let i = 0; i < quantidade; i++) {
            console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
        }
    }
};

function buscar_aluno () {
    let buscar_nome = prompt('Nome do aluno que deseja procurar: ');
    let verificacao = false;
    for (let aluno of alunos) {
        if (buscar_nome.toLowerCase() == aluno['nome'].toLowerCase()) {
            console.log(`Aluno: ${aluno['nome']}`);
            verificacao = true;
            let quantidade = aluno['notas'].length 
            for (let i = 0; i < quantidade; i++) {
                console.log(`Nota ${i+1}: ${aluno['notas'][i]}`);
            }
        }
    }
    if (verificacao == false) {
        console.log(`Aluno ${buscar_nome} não encontrado!`);
    }
};


while (true) {
    escolha = menu();
    if (escolha == '1') {
        add_alunos();
    }
    else if (escolha == '2') {
        listar_alunos();
    }
    else if (escolha == '3') {
        buscar_aluno();
    }
    else if (escolha == '4') {
        console.log('Fim do programa!');
        break;
    }
    else {
        console.log('Opção inválida!');
    }
}
