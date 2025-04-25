const prompt = require('prompt-sync')();

let alunos = [];
function add_alunos () {
    for (let y = 0; y <= 1; y++) {
        let nome = prompt('Nome do aluno: ');
        let notas = []
        for (let i = 1; i <= 3; i++) {
            let nota = prompt(`Nota ${i} do aluno: `);
            notas.push(parseFloat(nota));
        }
        alunos.push({nome: nome, notas: notas});
    }
    console.log(alunos);
}

add_alunos()