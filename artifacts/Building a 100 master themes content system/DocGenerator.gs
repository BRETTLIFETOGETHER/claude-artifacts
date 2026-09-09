/**
 * LIFETOGETHER CAMPAIGN DOC GENERATOR
 * Creates one Google Doc per row of the "Campaigns" sheet — no clicking, no Keyboard Maestro.
 * Handles thousands of docs safely by processing in batches with an auto-resume trigger.
 *
 * SETUP (one time, ~5 minutes):
 * 1. Upload Lifetogether_Master_Taxonomy.xlsx to Google Drive and open it AS a Google Sheet
 *    (File > Save as Google Sheets).
 * 2. Create ONE template Google Doc containing your four-part blueprint layout with merge
 *    fields written exactly like this anywhere in the doc:
 *    {{Title}} {{Subtitle}} {{Theme}} {{Audience}} {{LifeEvent}} {{TrustedGuide}}
 *    {{Format}} {{Framework}} {{FeltNeed}} {{Scripture}} {{CampaignID}}
 * 3. Create an empty Drive folder for output.
 * 4. In the Sheet: Extensions > Apps Script > paste this file > save.
 * 5. Paste the template Doc ID and output folder ID into CONFIG below.
 *    (The ID is the long string in the URL between /d/ and /edit.)
 * 6. Reload the Sheet. A "Lifetogether" menu appears. Click "Generate Docs".
 *
 * WHAT IT DOES per row where Status = "Ready":
 *  - copies the template
 *  - fills every merge field
 *  - names the doc "Title — Subtitle"
 *  - files it in a subfolder named after the Theme
 *  - writes the Doc URL back into the "Doc URL" column
 *  - sets Status to "Generated"
 * Apps Script caps a run at ~6 minutes, so this processes BATCH_SIZE rows per run and
 * installs a trigger that re-runs itself every few minutes until every row is done.
 * 2,500 docs finishes unattended in roughly an evening.
 */

const CONFIG = {
  TEMPLATE_DOC_ID: 'PASTE_TEMPLATE_DOC_ID_HERE',
  OUTPUT_FOLDER_ID: 'PASTE_OUTPUT_FOLDER_ID_HERE',
  SHEET_NAME: 'Campaigns',
  BATCH_SIZE: 40   // rows per run; safe for the 6-minute limit
};

function onOpen() {
  SpreadsheetApp.getUi().createMenu('Lifetogether')
    .addItem('Generate Docs (auto-resumes until done)', 'startGeneration')
    .addItem('Stop auto-resume', 'stopGeneration')
    .addToUi();
}

function startGeneration() {
  stopGeneration(); // clear old triggers
  ScriptApp.newTrigger('generateBatch').timeBased().everyMinutes(5).create();
  generateBatch(); // run the first batch immediately
}

function stopGeneration() {
  ScriptApp.getProjectTriggers().forEach(t => {
    if (t.getHandlerFunction() === 'generateBatch') ScriptApp.deleteTrigger(t);
  });
}

function generateBatch() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
  const data = sheet.getDataRange().getValues();
  const head = data[0];
  const col = name => head.indexOf(name);

  const c = {
    id: col('CampaignID'), theme: col('Theme'), title: col('Campaign Title'),
    sub: col('Subtitle'), aud: col('Audience'), evt: col('Life Event'),
    guide: col('Trusted Guide'), fmt: col('Format'), fw: col('Framework'),
    need: col('Felt Need'), scr: col('Scripture Anchor'),
    status: col('Status'), url: col('Doc URL')
  };

  const template = DriveApp.getFileById(CONFIG.TEMPLATE_DOC_ID);
  const outRoot = DriveApp.getFolderById(CONFIG.OUTPUT_FOLDER_ID);
  let done = 0;

  for (let r = 1; r < data.length && done < CONFIG.BATCH_SIZE; r++) {
    if (String(data[r][c.status]).trim() !== 'Ready') continue;
    const row = data[r];

    // one subfolder per theme
    const themeName = row[c.theme] || 'Uncategorized';
    const it = outRoot.getFoldersByName(themeName);
    const folder = it.hasNext() ? it.next() : outRoot.createFolder(themeName);

    const docName = row[c.sub] ? row[c.title] + ' — ' + row[c.sub] : row[c.title];
    const copy = template.makeCopy(docName, folder);
    const doc = DocumentApp.openById(copy.getId());
    const body = doc.getBody();

    const map = {
      '{{CampaignID}}': row[c.id], '{{Theme}}': themeName,
      '{{Title}}': row[c.title], '{{Subtitle}}': row[c.sub],
      '{{Audience}}': row[c.aud], '{{LifeEvent}}': row[c.evt],
      '{{TrustedGuide}}': row[c.guide], '{{Format}}': row[c.fmt],
      '{{Framework}}': row[c.fw], '{{FeltNeed}}': row[c.need],
      '{{Scripture}}': row[c.scr]
    };
    for (const k in map) body.replaceText(k, String(map[k] || ''));
    doc.saveAndClose();

    sheet.getRange(r + 1, c.url + 1).setValue(copy.getUrl());
    sheet.getRange(r + 1, c.status + 1).setValue('Generated');
    done++;
  }

  // all finished? remove the trigger
  const remaining = sheet.getDataRange().getValues()
    .slice(1).filter(row => String(row[c.status]).trim() === 'Ready').length;
  if (remaining === 0) stopGeneration();
}
