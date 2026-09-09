const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, AlignmentType, BorderStyle, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');

const NAVY = "1F3864";
const GREY = "595959";
const TW = 9360;

const P = (text, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 140, line: 276 },
  alignment: opts.align,
  children: [new TextRun({ text, font: "Calibri", size: opts.size ?? 21,
    bold: opts.bold, italics: opts.italics, color: opts.color })]
});

const H1 = (t) => new Paragraph({
  spacing: { before: 200, after: 120 },
  children: [new TextRun({ text: t, font: "Calibri", size: 26, bold: true, color: NAVY })],
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 4 } }
});

const H2 = (t) => new Paragraph({
  spacing: { before: 180, after: 80 },
  children: [new TextRun({ text: t, font: "Calibri", size: 22, bold: true, color: NAVY })]
});

const BUL = (t) => new Paragraph({
  bullet: { level: 0 }, spacing: { after: 60, line: 264 },
  children: [new TextRun({ text: t, font: "Calibri", size: 20 })]
});

function cell(text, { bold = false, fill = null, w, align = AlignmentType.LEFT, size = 19 } = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({ alignment: align, spacing: { after: 0 },
      children: [new TextRun({ text, font: "Calibri", size, bold,
        color: fill === NAVY ? "FFFFFF" : "000000" })] })]
  });
}

function table(headers, rows, widths) {
  return new Table({
    width: { size: TW, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({
        tableHeader: true,
        children: headers.map((h, i) => cell(h, { bold: true, fill: NAVY, w: widths[i] }))
      }),
      ...rows.map((r, ri) => new TableRow({
        children: r.map((c, i) => cell(c, {
          w: widths[i],
          fill: ri % 2 === 1 ? "F2F2F2" : null,
          align: i === 0 ? AlignmentType.LEFT : AlignmentType.LEFT
        }))
      }))
    ]
  });
}

const children = [];

children.push(new Paragraph({
  spacing: { after: 40 },
  children: [new TextRun({ text: "RON BLUE INSTITUTE", font: "Calibri", size: 18, bold: true, color: GREY, characterSpacing: 40 })]
}));
children.push(new Paragraph({
  spacing: { after: 40 },
  children: [new TextRun({ text: "Fulfillment Rate Card Request", font: "Calibri", size: 34, bold: true, color: NAVY })]
}));
children.push(P("Prepared for the 30-minute call · Print, kitting, storage and outbound fulfillment for a six-title church campaign line · August 2026", { size: 19, italics: true, color: GREY, after: 260 }));

children.push(H1("What we need from this call"));
children.push(P("We are launching a six-title church campaign product line built around Ron Blue's financial stewardship material. Each title generates a family of print SKUs plus assembled kits. We need a complete rate card — including the exception charges — so we can set retail pricing that does not lose money and lock a production partner for the full run."));
children.push(P("Please come to the call ready to quote the line items in Section 3. We are not looking for a range. We are looking for numbers we can put in a pro forma.", { bold: true }));

children.push(H1("1. Scope — what has to be printed, stored and shipped"));
children.push(P("Six campaign titles: God Owns It All, Master Your Money, Generous Living, Splitting Heirs, This Changes Everything, How Much Is Enough. Each title carries the same SKU architecture:"));
children.push(table(
  ["Item", "Trim / Format", "Approx. Pages", "Est. Annual Units per Title"],
  [
    ["Trade Book", "5.5 × 8.5 paperback, 4c cover", "208", "20,000 – 25,000"],
    ["40-Day Devotional", "5.5 × 8.5 paperback, 4c cover", "176", "20,000 – 25,000"],
    ["Participant Guide", "7 × 9 workbook, 4c cover", "128", "20,000 – 25,000"],
    ["Leader Guide", "7 × 9 workbook", "64", "4,000 – 6,000"],
    ["Student Devotional", "5.5 × 8.5 paperback, 4c cover", "144", "10,000 – 12,000"],
    ["Student Participant Guide", "7 × 9 workbook, 4c cover", "112", "10,000 – 12,000"],
    ["Student Leader Guide", "7 × 9 workbook", "64", "2,000 – 3,000"],
    ["Church Campaign Handbook", "7 × 9 paperback", "96", "2,000 – 3,000"],
    ["Children's Leader Kit", "Boxed, mixed components", "n/a", "1,000 – 2,000"]
  ],
  [2600, 2900, 1500, 2360]
));
children.push(P("That is 54 physical SKUs across the line. Volumes above are planning estimates from our Year 1 model, not commitments. Please quote at 5,000 / 10,000 / 25,000 break points so we can see the curve.", { size: 19, italics: true, color: GREY }));

children.push(H1("2. Kits — what has to be assembled"));
children.push(P("Five kit configurations per title, each needing its own carton, barcode and SKU. Assume kits are pre-built at receipt, not built on demand — but quote both ways if the difference is material."));
children.push(table(
  ["Kit", "Contents", "Est. Weight"],
  [
    ["Personal Kit", "1 Trade Book, 1 Devotional, 1 Participant Guide", "~3.0 lb"],
    ["Group Kit", "10 Participant Guides, 2 Leader Guides, 1 video access card", "~7.1 lb"],
    ["Group Kit Plus", "10 Participant Guides, 2 Leader Guides, 10 Devotionals, 1 video access card", "~13.6 lb"],
    ["Student Group Kit", "10 Student Participant Guides, 2 Student Leader Guides, 1 video access card", "~6.6 lb"],
    ["Church Campaign Kit", "One of each print item across adult, student, children and pastor, plus digital access card", "~7.1 lb"]
  ],
  [1900, 5560, 1900]
));

children.push(H1("3. The rate card — please price every line"));
children.push(P("This is the section we need filled in. Blank lines are as useful to us as high ones — we just need to know what is chargeable."));

children.push(H2("Receiving and storage"));
children.push(BUL("Inbound receiving — per pallet, and per carton"));
children.push(BUL("Palletizing / restacking, if charged separately"));
children.push(BUL("Storage — per pallet per month, and any minimum pallet commitment"));
children.push(BUL("Long-term storage surcharge, and at what age it triggers"));

children.push(H2("Kitting and assembly"));
children.push(BUL("Kitting labor — per kit, pre-built at receipt"));
children.push(BUL("Kitting labor — per kit, built on demand at time of order"));
children.push(BUL("Shrink wrap, banding, or insert placement, if charged separately"));
children.push(BUL("Barcode / SKU setup — one time, per SKU"));

children.push(H2("Pick, pack and ship"));
children.push(BUL("Pick fee — first unit in an order"));
children.push(BUL("Pick fee — each additional unit"));
children.push(BUL("Corrugate — standard carton, by size"));
children.push(BUL("Corrugate — custom printed / branded carton, and the minimum order to get one"));
children.push(BUL("Dunnage and void fill"));
children.push(BUL("Label and packing slip"));
children.push(BUL("Order transaction or administrative fee, per order"));

children.push(H2("Freight"));
children.push(BUL("Negotiated ground rate — per pound, by zone, and your minimum charge"));
children.push(BUL("Residential delivery surcharge (most church orders ship to a church address, some to a home)"));
children.push(BUL("Address correction fee"));
children.push(BUL("Oversize or overweight thresholds and surcharges"));
children.push(BUL("Peak season surcharge — dates and amount"));
children.push(BUL("LTL / pallet rate for bulk church orders of 25+ kits"));

children.push(H2("Returns and exceptions"));
children.push(BUL("Return receipt and inspection — per return"));
children.push(BUL("Restock to sellable — per unit"));
children.push(BUL("Disposal or destruction — per unit"));
children.push(BUL("Rush or same-day pick — surcharge and cutoff time"));
children.push(BUL("Any monthly account, WMS, or platform minimum"));
children.push(BUL("Integration fee for our storefront, and which platforms you already connect to"));

children.push(H1("4. Two questions we need answered directly"));
children.push(P("First: give us the all-in landed cost of one Group Kit, printed, stored for six months, picked, packed and delivered to a single church address in the continental US. One number. That single figure determines our retail price.", { bold: true }));
children.push(P("Second: we have seen a fulfillment charge of roughly $172 on an inbound shipment. Please walk us through how that number was built — which of the line items above it contains, and how many units it covered. We need to understand the anatomy of a charge before we can model a business around it."));

children.push(H1("5. Terms we want to discuss"));
children.push(BUL("Volume tiers and the annual commitment required to reach each one"));
children.push(BUL("Payment terms, and whether print and fulfillment can be billed on the same terms"));
children.push(BUL("Whether you will hold price for a full campaign season once we launch"));
children.push(BUL("Lead time from PO to pallets on your floor, and from order to ship"));
children.push(BUL("What you need from us to quote firm rather than indicative"));

children.push(new Paragraph({
  spacing: { before: 320 },
  border: { top: { style: BorderStyle.SINGLE, size: 6, color: "BFBFBF", space: 8 } },
  children: [new TextRun({ text: "Status: proposed pricing architecture, not approved. Unit volumes are planning estimates from the Year 1 model and are subject to change. This document is a request for quotation and does not constitute a purchase commitment.",
    font: "Calibri", size: 17, italics: true, color: GREY })]
}));

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 21 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 } } },
    children
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/home/claude/rbi/RBI_Fulfillment_Rate_Card_Request.docx', b);
  console.log('ok');
});
