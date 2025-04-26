function normalizeUrl(url) {
  if (!/^https?:\/\//i.test(url)) {
    return 'https://' + url;
  }
  return url;
}

document.getElementById('scan-btn').onclick = () => {
  document.getElementById('scanner').style.display = 'block';
  document.getElementById('manual-url').style.display = 'none';
  document.getElementById('analyze-btn').style.display = 'none';

  const qr = new Html5Qrcode("scanner");
  qr.start({ facingMode: "environment" }, { fps: 10, qrbox: 250 }, async (url) => {
    qr.stop();
    analyzeURL(url);
  });
};

document.getElementById('url-btn').onclick = () => {
  document.getElementById('scanner').style.display = 'none';
  document.getElementById('manual-url').style.display = 'block';
  document.getElementById('analyze-btn').style.display = 'inline-block';
};

document.getElementById('analyze-btn').onclick = () => {
  const url = document.getElementById('manual-url').value;
  analyzeURL(url);
};

async function analyzeURL(rawUrl) {
  const url = normalizeUrl(rawUrl);

  const res = await fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url })
  });

  const data = await res.json();
  const resultEl = document.getElementById('result');

  if (data.error) {
    resultEl.innerHTML = `<p class="text-red-600">❌ Error: ${data.error}</p>`;
    return;
  }

  resultEl.innerHTML = `
    <div class="p-4 border rounded-md ${data.safe ? 'border-green-400 bg-green-50' : 'border-red-400 bg-red-50'}">
      <p class="${data.safe ? 'text-green-700' : 'text-red-700'} font-semibold">
        ${data.safe ? '✅ Enlace seguro' : '❌ Enlace malicioso o sospechoso'}
      </p>
      <p class="text-sm mt-1">
        <a href="${url}" class="underline text-blue-600" target="_blank">${url}</a>
      </p>
      <ul class="mt-3 text-gray-700 text-sm space-y-1">
        <li>🟢 Harmless: <strong>${data.harmless || 0}</strong></li>
        <li>🟡 Sospechosos: <strong>${data.suspicious || 0}</strong></li>
        <li>🔴 Maliciosos: <strong>${data.malicious || 0}</strong></li>
        <li>🕵️‍♂️ No detectados: <strong>${data.undetected || 0}</strong></li>
      </ul>
      <p class="text-sm mt-2">
        🔗 <a href="${data.vt_url}" target="_blank" class="text-blue-600 underline">Ver informe completo en VirusTotal</a>
      </p>
    </div>
  `;
}
