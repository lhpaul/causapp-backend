'use strict';

var express = require('express');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();
var Q = require('q');

var webdriver = require('selenium-webdriver');

refreshCookies();
var CronJob = require('cron').CronJob;
new CronJob('0 */10 * * * *', function(){
    refreshCookies();
}, null, true, 'America/Los_Angeles');


var cookies = null;

function refreshCookies(){
  console.log('refreshing cookies');
  return;
  var driver = new webdriver.Builder().
   withCapabilities(webdriver.Capabilities.chrome()).
   build();
  driver.get('http://civil.poderjudicial.cl/CIVILPORWEB/');
  driver.manage().getCookies().then(function(data_cookies){
    cookies = '';
    for(var i = 0; i < data_cookies.length; i++){
      cookies += data_cookies[i].name + '=' + data_cookies[i].value + '; ';
    }
    // console.log(cookies);
    // console.log('cookies listas');
  });
  driver.quit();
}

var getData = function(rut, veref){
  var deferred = Q.defer();
  var options = {
    url: 'http://civil.poderjudicial.cl/CIVILPORWEB/AtPublicoDAction.do',
    headers: { Cookie: cookies },
    qs: {
      TIP_Consulta : 2,
      TIP_Lengueta : 'tdTres',
      RUC_Tribunal : '3',
      FEC_Desde : '20/11/2014',
      FEC_Hasta : '20/11/2014',
      SEL_Litigantes : 0,
      irAccionAtPublico : 'Consultaee',
      RUT_Consulta : rut,
      RUT_DvConsulta : veref,
      COD_Tribunal:259
    }
  };
  request(options, function(error, response, html){
    if(!error){
      var data = [];
      var $ = cheerio.load(html);
      $('#gridHeadAddTabla2').find('tr').each(function(i, elem) {
        var obj = {};
        var tds = $(this).find($('td'));
        obj.link = tds[0].children[0].next.attribs.href;
        obj.rol = tds[0].children[0].next.children[0].data;
        obj.fecha = tds[1].children[0].data;
        obj.caratulado = tds[2].children[0].data;
        obj.tribunal = tds[3].children[0].data;
        data.push(obj);
      });
      deferred.resolve(data);
    }
  });

  return deferred.promise;
};

app.get('/user/:rut', function(req, res){
  var rut = req.params.rut;
  var length = rut.length;

  res.json([
    {link: 'wwww.algo.cl', rol: 'RES2233223', fecha: '22/11/2012', caratulado: 'Caratulado Algo', tribunal: 'Tribunal de Santiago'},
    {link: 'wwww.emol.cl', rol: 'RES256754', fecha: '02/07/2013', caratulado: 'Caratulado Otro', tribunal: 'Tribunal de Calama'}
    ]);
  // getData(rut.slice(0,length-1),rut.slice(length-1,length)).then(function(data){
  //     res.json(data);
  // });

});

app.listen('8081');
console.log('Magic happens on port 8081');
exports = module.exports = app;