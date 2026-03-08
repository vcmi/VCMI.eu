---
hide:
  - navigation
  - toc
---

# Lobby

This page shows current lobby statistics.

<div class="md-typeset">
  <div id="lobby_stats_box">
    <div id="lobby_stat_loading">Loading...</div>
    <div id="lobby_stat_error" style="display:none;color:#a00"></div>

    <div id="lobby_stat_content" style="display:none;">
      

      <table id="tbl_combined">
        <thead>
          <tr>
            <th colspan="2">Overview</th>
            <th colspan="2">Game Count</th>
            <th colspan="2">Lobby Count</th>
            <th colspan="2">Online Players Count</th>
          </tr>
        </thead>
        <tbody id="tbody_combined"></tbody>
      </table>
      
      <h2>Rooms</h2>
      <table id="tbl_rooms">
        <thead>
          <tr>
            <th>Status</th>
            <th>Created</th>
            <th>Description</th>
            <th>Player Limit</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  </div>
</div>

<script>
(function(){
  window.API_URL = "{{ config.extra.api_url | default('') }}";
  window.API_ENDPOINT_STATS = "{{ config.extra.api_endpoint_stats | default('') }}";
  window.API_ENDPOINT_ROOMS = "{{ config.extra.api_endpoint_rooms | default('') }}";
  
  const url = window.API_URL + window.API_ENDPOINT_STATS;

  const elLoading = document.getElementById('lobby_stat_loading');
  const elContent = document.getElementById('lobby_stat_content');
  const elError = document.getElementById('lobby_stat_error');

  function setError(msg){ if (elLoading) elLoading.style.display='none'; if (elError) { elError.style.display='block'; elError.textContent = msg; } }

  function objToPairs(obj){ return Object.keys(obj||{}).map(k=>[k, obj[k]]); }

  function formatIsoToLocal(iso){
    if (iso === null || iso === undefined) return '';
    // try number
    let d = null;
    if (typeof iso === 'number') d = new Date(iso);
    else {
      // try numeric string
      const n = Number(iso);
      if (!isNaN(n) && String(n).length > 9) d = new Date(n);
      else d = new Date(iso);
    }
    if (isNaN(d)) return String(iso);
    return d.toLocaleString();
  }

  const KEY_LABELS = {
    apiVersion: 'API Version',
    lobbyStartTime: 'Lobby Start',
    lobbyVersion: 'Lobby Version',
    registeredPlayersCount: 'Registered Players',
    server: 'Server',
    current: 'Current',
    total: 'Total'
  };

  function prettyKey(k){
    if (!k) return '';
    if (KEY_LABELS[k]) return KEY_LABELS[k];
    let s = String(k).replace(/_/g, ' ');
    s = s.replace(/([a-z])([A-Z])/g, '$1 $2');
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  function sortLastEntriesInPlace(pairs){
    if (!pairs || !pairs.length) return pairs;
    // collect indices and entries for keys starting with 'last'
    const lastIdx = [];
    const lastEntries = [];
    pairs.forEach((p, i)=>{ if (/^last/i.test(p[0])){ lastIdx.push(i); lastEntries.push(p); } });
    if (lastEntries.length < 2) return pairs;

    const unitOrder = (key)=>{
      const k = String(key).toLowerCase();
      if (/min/i.test(k)) return 60;
      if (/hour|hr/i.test(k)) return 3600;
      if (/day/i.test(k)) return 86400;
      if (/week/i.test(k)) return 7*86400;
      if (/month/i.test(k)) return 30*86400;
      if (/year/i.test(k)) return 365*86400;
      return Number.MAX_SAFE_INTEGER; // unknown go last
    };

    lastEntries.sort((a,b)=>{
      const va = unitOrder(a[0]);
      const vb = unitOrder(b[0]);
      if (va !== vb) return va - vb;
      // fallback: try numeric value comparison if parseable
      const na = Number(a[1]);
      const nb = Number(b[1]);
      if (!isNaN(na) && !isNaN(nb)) return na - nb;
      return String(a[0]).localeCompare(String(b[0]));
    });

    // put sorted lastEntries back into original positions
    const out = pairs.slice();
    lastIdx.forEach((idx, i)=>{ out[idx] = lastEntries[i]; });
    return out;
  }

  function fillCombinedTable(overview, gameCount, lobbyCount, onlinePlayersCount){
    const tbody = document.getElementById('tbody_combined');
    tbody.innerHTML = '';
    
    let ov = objToPairs(overview || {});
    // format lobbyStartTime if present
    for(const p of ov){ if (p[0] === 'lobbyStartTime') p[1] = formatIsoToLocal(p[1]); }
    ov = sortLastEntriesInPlace(ov);

    let gc = objToPairs(gameCount);
    let lc = objToPairs(lobbyCount);
    let opc = objToPairs(onlinePlayersCount);
    gc = sortLastEntriesInPlace(gc);
    lc = sortLastEntriesInPlace(lc);
    opc = sortLastEntriesInPlace(opc);
    
    const maxRows = Math.max(ov.length, gc.length, lc.length, opc.length);
    
    for(let i = 0; i < maxRows; i++){
      const tr = document.createElement('tr');
      
      // Overview
      if(ov[i]){ 
        const td1 = document.createElement('td'); td1.textContent = prettyKey(ov[i][0]); tr.appendChild(td1);
        const td2 = document.createElement('td'); td2.textContent = ov[i][1]; tr.appendChild(td2);
      } else {
        tr.appendChild(document.createElement('td'));
        tr.appendChild(document.createElement('td'));
      }
      
      // Game Count
      if(gc[i]){ 
        const td1 = document.createElement('td'); td1.textContent = prettyKey(gc[i][0]); tr.appendChild(td1);
        const td2 = document.createElement('td'); td2.textContent = gc[i][1]; tr.appendChild(td2);
      } else {
        tr.appendChild(document.createElement('td'));
        tr.appendChild(document.createElement('td'));
      }
      
      // Lobby Count
      if(lc[i]){ 
        const td1 = document.createElement('td'); td1.textContent = prettyKey(lc[i][0]); tr.appendChild(td1);
        const td2 = document.createElement('td'); td2.textContent = lc[i][1]; tr.appendChild(td2);
      } else {
        tr.appendChild(document.createElement('td'));
        tr.appendChild(document.createElement('td'));
      }
      
      // Online Players Count
      if(opc[i]){ 
        const td1 = document.createElement('td'); td1.textContent = prettyKey(opc[i][0]); tr.appendChild(td1);
        const td2 = document.createElement('td'); td2.textContent = opc[i][1]; tr.appendChild(td2);
      } else {
        tr.appendChild(document.createElement('td'));
        tr.appendChild(document.createElement('td'));
      }
      
      tbody.appendChild(tr);
    }
  }

  function fillArrayTable(id, arr){
    const tbody = document.getElementById(id).getElementsByTagName('tbody')[0];
    tbody.innerHTML = '';
    if (!arr || !arr.length){ const tr = document.createElement('tr'); const td = document.createElement('td'); td.colSpan=2; td.textContent='(none)'; tr.appendChild(td); tbody.appendChild(tr); return; }
    arr.forEach(item=>{
      const tr = document.createElement('tr');
      const td1 = document.createElement('td'); td1.textContent = item.name || item.id || ''; tr.appendChild(td1);
      const td2 = document.createElement('td'); td2.textContent = JSON.stringify(item); tr.appendChild(td2);
      tbody.appendChild(tr);
    });
  }

  fetch(url, { method: 'GET', credentials: 'omit' })
    .then(resp=>{ if (!resp.ok) throw new Error('Network response not ok'); return resp.json(); })
    .then(json=>{
      if (elLoading) elLoading.style.display='none';
      fillCombinedTable({ lobbyStartTime: json.lobbyStartTime, registeredPlayersCount: json.registeredPlayersCount }, json.gameCount, json.lobbyCount, json.onlinePlayersCount);

      if (elContent) elContent.style.display='block';
    })
    .catch(err=>{ console.debug('Could not fetch lobby stats:', err); setError('Failed to load stats'); });

  // fetch rooms
  const roomsUrl = window.API_URL + window.API_ENDPOINT_ROOMS ;
  function statusEmoji(s){
    // 1=PUBLIC,2=PRIVATE,3=BUSY
    if (s === 1) return '🟢';
    if (s === 2) return '🔑';
    if (s === 3) return '⚔️';
    return '';
  }

  function renderRooms(json){
    const tbody = document.getElementById('tbl_rooms').getElementsByTagName('tbody')[0];
    tbody.innerHTML = '';
    if (!json || !Array.isArray(json.rooms)) return;
    // filter only PUBLIC(1), PRIVATE(2), BUSY(3)
    const rows = json.rooms.filter(r=>[1,2,3].includes(r.status));
    // sort by createdAt desc
    rows.sort((a,b)=>{ const da = Date.parse(a.createdAt); const db = Date.parse(b.createdAt); return (isNaN(db)?0:db) - (isNaN(da)?0:da); });
    rows.forEach(r=>{
      const tr = document.createElement('tr');
      const tdStatus = document.createElement('td'); tdStatus.textContent = statusEmoji(r.status); tr.appendChild(tdStatus);
      const tdCreated = document.createElement('td'); tdCreated.textContent = (r.createdAt? new Date(r.createdAt).toLocaleString(): ''); tr.appendChild(tdCreated);
      const tdDesc = document.createElement('td'); tdDesc.textContent = r.description || ''; tr.appendChild(tdDesc);
      const tdLimit = document.createElement('td'); tdLimit.textContent = r.playerLimit || ''; tr.appendChild(tdLimit);
      tbody.appendChild(tr);
    });
  }

  fetch(roomsUrl, { method: 'GET', credentials: 'omit' })
    .then(resp=>{ if (!resp.ok) throw new Error('Rooms response not ok'); return resp.json(); })
    .then(json=>{ renderRooms(json); })
    .catch(err=>{ console.debug('Could not fetch rooms:', err); });

})();
</script>
