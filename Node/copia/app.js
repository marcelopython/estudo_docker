const express = require('express')

const app = express()
const port = 3000

app.get('/', (req, res)=>{
    res.send('Olá minha imagem teste')
})

app.listen(port, ()=>{
    console.log('executando: '+port)
})