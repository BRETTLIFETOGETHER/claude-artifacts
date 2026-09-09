const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak, HeadingLevel
} = require('docx');
const fs = require('fs');

const WHITE="FFFFFF"; const DGRAY="2B2B2B"; const MGRAY="555555"; const LGRAY="F5F5F5";

function sp(b=60,a=60){return new Paragraph({spacing:{before:b,after:a},children:[new TextRun("")]})}
function pb(){return new Paragraph({children:[new PageBreak()]})}
function hrule(c){return new Paragraph({border:{bottom:{style:BorderStyle.SINGLE,size:8,color:c,space:1}},spacing:{before:60,after:60}})}

function bookCover(title,subtitle,author,outlineNum,theme,dk,med,lt){
  const b={style:BorderStyle.SINGLE,size:8,color:dk};
  return [
    sp(320,0),
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[new TableRow({children:[new TableCell({
      borders:{top:b,bottom:b,left:b,right:b},
      shading:{fill:dk,type:ShadingType.CLEAR},
      margins:{top:280,bottom:280,left:360,right:360},
      children:[
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:60},children:[new TextRun({text:title,bold:true,size:52,font:"Arial",color:WHITE})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:60},children:[new TextRun({text:subtitle,size:22,font:"Arial",color:lt,italics:true})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},children:[new TextRun({text:author,size:20,font:"Arial",color:lt})]}),
      ]
    })]})]})
    ,sp(60,0),
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[new TableRow({children:[new TableCell({
      borders:{top:{style:BorderStyle.SINGLE,size:4,color:med},bottom:{style:BorderStyle.SINGLE,size:4,color:med},left:{style:BorderStyle.SINGLE,size:4,color:med},right:{style:BorderStyle.SINGLE,size:4,color:med}},
      shading:{fill:lt,type:ShadingType.CLEAR},
      margins:{top:160,bottom:160,left:360,right:360},
      children:[
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:40},children:[new TextRun({text:`OUTLINE ${outlineNum}`,bold:true,size:28,font:"Arial",color:dk})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},children:[new TextRun({text:theme,size:21,font:"Arial",color:med,italics:true})]}),
      ]
    })]})]})
    ,sp(80,40),
    new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:40},children:[new TextRun({text:"40-Day Reading Plan  ·  6 Sessions  ·  ~6–7 Days Per Session",size:19,font:"Arial",color:MGRAY})]}),
    hrule(med),sp(60,60)
  ];
}

function sessionBanner(sn,title,subtitle,desc,chapters,dk,med,lt){
  const b={style:BorderStyle.SINGLE,size:4,color:dk};
  const ob={style:BorderStyle.SINGLE,size:1,color:"CCCCCC"};
  return [
    pb(),
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[new TableRow({children:[new TableCell({
      borders:{top:b,bottom:b,left:b,right:b},
      shading:{fill:dk,type:ShadingType.CLEAR},
      margins:{top:140,bottom:140,left:240,right:240},
      children:[
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:30},children:[new TextRun({text:`SESSION ${sn}`,bold:true,size:20,font:"Arial",color:lt})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:30},children:[new TextRun({text:title,bold:true,size:30,font:"Arial",color:WHITE})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},children:[new TextRun({text:subtitle,size:20,font:"Arial",color:lt,italics:true})]}),
      ]
    })]})]})
    ,sp(40,0),
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[6600,2760],rows:[new TableRow({children:[
      new TableCell({
        borders:{top:{style:BorderStyle.NONE},bottom:{style:BorderStyle.NONE},left:{style:BorderStyle.SINGLE,size:6,color:med},right:{style:BorderStyle.NONE}},
        shading:{fill:LGRAY,type:ShadingType.CLEAR},
        margins:{top:100,bottom:100,left:180,right:140},
        children:[new Paragraph({children:[new TextRun({text:desc,size:18,font:"Arial",color:DGRAY,italics:true})]})]
      }),
      new TableCell({
        borders:{top:{style:BorderStyle.NONE},bottom:{style:BorderStyle.NONE},left:ob,right:{style:BorderStyle.NONE}},
        shading:{fill:lt,type:ShadingType.CLEAR},
        margins:{top:100,bottom:100,left:160,right:120},
        children:[
          new Paragraph({spacing:{before:0,after:30},children:[new TextRun({text:"Chapters / Source",bold:true,size:17,font:"Arial",color:dk})]}),
          new Paragraph({children:[new TextRun({text:chapters,size:17,font:"Arial",color:MGRAY})]}),
        ]
      }),
    ]})]})
    ,sp(50,30)
  ];
}

function dayCard(dn,title,subtitle,desc,verses,dk,med,lt){
  const ob={style:BorderStyle.SINGLE,size:1,color:"DDDDDD"};
  return [
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[900,8460],rows:[
      new TableRow({children:[
        new TableCell({
          borders:{top:{style:BorderStyle.SINGLE,size:2,color:dk},bottom:{style:BorderStyle.SINGLE,size:2,color:dk},left:{style:BorderStyle.SINGLE,size:2,color:dk},right:{style:BorderStyle.SINGLE,size:2,color:dk}},
          shading:{fill:dk,type:ShadingType.CLEAR},
          margins:{top:100,bottom:100,left:80,right:80},
          verticalAlign:"center",
          children:[
            new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},children:[new TextRun({text:"DAY",size:14,font:"Arial",color:lt,bold:true})]}),
            new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},children:[new TextRun({text:String(dn),size:34,font:"Arial",color:WHITE,bold:true})]}),
          ]
        }),
        new TableCell({
          borders:{top:{style:BorderStyle.SINGLE,size:2,color:dk},bottom:{style:BorderStyle.SINGLE,size:2,color:dk},left:{style:BorderStyle.NONE},right:{style:BorderStyle.SINGLE,size:2,color:dk}},
          shading:{fill:lt,type:ShadingType.CLEAR},
          margins:{top:90,bottom:90,left:180,right:140},
          children:[
            new Paragraph({spacing:{before:0,after:20},children:[new TextRun({text:title,bold:true,size:22,font:"Arial",color:dk})]}),
            new Paragraph({spacing:{before:0,after:0},children:[new TextRun({text:subtitle,size:19,font:"Arial",color:med,italics:true})]}),
          ]
        }),
      ]}),
      new TableRow({children:[
        new TableCell({
          borders:{top:{style:BorderStyle.NONE},bottom:ob,left:ob,right:ob},
          shading:{fill:WHITE,type:ShadingType.CLEAR},
          margins:{top:80,bottom:80,left:80,right:80},
          children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:"✦",size:18,font:"Arial",color:med})]})]
        }),
        new TableCell({
          borders:{top:{style:BorderStyle.NONE},bottom:ob,left:{style:BorderStyle.SINGLE,size:1,color:"EEEEEE"},right:ob},
          shading:{fill:WHITE,type:ShadingType.CLEAR},
          margins:{top:90,bottom:90,left:180,right:140},
          children:[
            new Paragraph({spacing:{before:0,after:50},children:[new TextRun({text:desc,size:18,font:"Arial",color:DGRAY})]}),
            new Paragraph({spacing:{before:0,after:0},children:[
              new TextRun({text:"Key Verses:  ",bold:true,size:17,font:"Arial",color:med}),
              new TextRun({text:verses,size:17,font:"Arial",color:MGRAY,italics:true}),
            ]}),
          ]
        }),
      ]}),
    ]}),
    sp(36,36)
  ];
}

function buildBook(coverArgs, outlines, dk, med, lt, filename){
  const children = [];
  outlines.forEach((outline, oi) => {
    const {num,theme,sessions} = outline;
    bookCover(...coverArgs, num, theme, dk, med, lt).forEach(n=>children.push(n));
    sessions.forEach(sess => {
      const {sn,title,subtitle,desc,chapters,days} = sess;
      sessionBanner(sn,title,subtitle,desc,chapters,dk,med,lt).forEach(n=>children.push(n));
      days.forEach(([dn,t,st,d,v])=> dayCard(dn,t,st,d,v,dk,med,lt).forEach(n=>children.push(n)));
    });
  });

  const doc = new Document({
    styles:{
      default:{document:{run:{font:"Arial",size:20}}},
      paragraphStyles:[
        {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,
         run:{size:32,bold:true,font:"Arial",color:dk},
         paragraph:{spacing:{before:240,after:160},outlineLevel:0}},
      ]
    },
    sections:[{
      properties:{page:{size:{width:12240,height:15840},margin:{top:864,right:864,bottom:864,left:864}}},
      children
    }]
  });
  Packer.toBuffer(doc).then(buf=>{
    const p=`/mnt/user-data/outputs/${filename}`;
    fs.writeFileSync(p,buf);
    console.log(`✓ ${filename}`);
  });
}

module.exports = {buildBook};
