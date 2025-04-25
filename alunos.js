const prompt = require('prompt-sync')();

let alunos = [];
function menu () {
    console.log('MENU');
    console.log(' 1. adicionar aluno\n 2. listar alunos');
}
function add_alunos () {

    let nome = prompt('Nome do aluno: ');
    let notas = []
    for (let i = 1; i <= 3; i++) {
        let nota = prompt(`Nota ${i} do aluno: `);
        notas.push(parseFloat(nota));
    }
    console.log(`Aluno ${nome} adicionado com sucesso!`)
    alunos.push({nome: nome, notas: notas});
}
menu();