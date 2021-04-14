const express = require('express');
const bcryptjs = require('bcryptjs');
const session = require('express-session')
const SessionStore = require('express-mysql-session')(session);
const csrf = require('csurf');
const fs = require('fs');
const bodyparser = require('body-parser');
const cookieParser = require('cookie-parser');
const path = require('path');
const expressFileUpload = require('express-fileupload');

const app = express()
app.use(expressFileUpload())

app.use('/public', express.static(path.join(__dirname, 'public')))
app.set('view engine', 'ejs')
app.set('views', 'views')

/**
 * controllers
 * models
 * views
 * middlewares
 * routes
 */

app.get('/url', (req, res, next) => {
    return res.render('', {
        
    });
});

app.use((req, res, next) => {
    res.locals.loggedin = req.session.loggedin;
    res.locals.user = req.session.user;
    res.setHeader('Access-Control-Allow-Origin', '*');

})

app.listen(8000, () => {
    console.log(`Listening to the port : ${port}`);
});


