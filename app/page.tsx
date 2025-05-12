'use client';
import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import "./page.css";

const calcularEspessuras = ({ N, CBRn, CBRSB, KR, KB, KSB }) => {
  N = Number(N);
  CBRn = Number(CBRn);
  CBRSB = Number(CBRSB);
  KR = Number(KR);
  KB = Number(KB);
  KSB = Number(KSB);

  let R;
  if (N <= 1e6) R = 5;
  else if (N <= 5e6) R = 7.5;
  else if (N <= 1e7) R = 10;
  else R = 12.5;

  const H20 = 77.67 * Math.pow(N, 0.0482) * Math.pow(CBRSB, -0.598);
  const Hn = 77.67 * Math.pow(N, 0.0482) * Math.pow(CBRn, -0.598);

  let B = (H20 - R * KR) / KB;
  if (B <= 15) B = 15;

  let h20 = (Hn - R * KR - B * KB) / KSB;
  if (h20 <= 15) h20 = 15;

  return { R, B, h20 };
};

export default function Home() {
  const [inputs, setInputs] = useState({ N: '', CBRn: '', CBRSB: '', KR: '', KB: '', KSB: '' });
  const [resultados, setResultados] = useState(null);

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    const { N, CBRn, CBRSB, KR, KB, KSB } = inputs;
    if ([N, CBRn, CBRSB, KR, KB, KSB].every(val => val !== '')) {
      const res = calcularEspessuras({ N, CBRn, CBRSB, KR, KB, KSB });
      setResultados(res);
    }
  };

  return (
    <main className="p-6 max-w-4xl mx-auto space-y-8">
      {/* Header Section */}
      <header className="header">
        <div className="header-logos">
          <img src="/upe_poli.png" alt="Logo POLI/UPE" className="header-logo" />
          <img src="/ppges.png" alt="Logo PPGES" className="header-logo" />
        </div>
        <h1 className="header-title">Dimensionamento de Pavimentos Flexíveis</h1>
        <p className="header-description">
          Esta ferramenta foi desenvolvida para auxiliar no cálculo das espessuras das camadas de pavimentos flexíveis,
          com base nas diretrizes do DNIT. Insira os parâmetros abaixo para visualizar os resultados e o gráfico das camadas.
        </p>
        <Card>
        <img src="/tabela_dnit.png" alt="Tabela DNIT" className="header-dnit" />
        </Card>
      </header>

      {/* Input Form Section */}
      <Card>
        <h2 className="header-title">Parâmetros de Entrada</h2>
        <div className="grid-container">
          {[
            { name: 'N', label: 'Número de solicitações (N)' },
            { name: 'CBRn', label: 'CBR Subleito (CBRn)' },
            { name: 'CBRSB', label: 'CBR Sub-base (CBRSB)' },
            { name: 'KR', label: 'KR (Coef. Revestimento)' },
            { name: 'KB', label: 'KB (Coef. Base)' },
            { name: 'KSB', label: 'KSB (Coef. Sub-base)' },
          ].map(({ name, label }) => (
            <div key={name} className="text-center">
              <Label htmlFor={name} className="text-blue-700">{label}</Label>
              <Input id={name} name={name} value={inputs[name]} onChange={handleChange} type="number" className="border-blue-300" />
            </div>
          ))}
        </div>
        <Button onClick={handleSubmit} className="w-full sm:w-auto mt-6 bg-blue-500 hover:bg-blue-600 text-white">
          Calcular Espessuras
        </Button>
      </Card>

      {/* Results Section */}
      {resultados && (
        <Card className="p-6 shadow-lg bg-gradient-to-r from-green-100 to-green-50 rounded-lg">
          <h2 className="header-description2">Resultados</h2>
          <ul className="header-description2">
            <p><strong>Revestimento (R):</strong> {resultados.R} cm</p>
            <p><strong>Base (B):</strong> {resultados.B.toFixed(2)} cm</p>
            <p><strong>Sub-base (h20):</strong> {resultados.h20.toFixed(2)} cm</p>
          </ul>

          <div className="layered-columns">
            <div className="sub-base" style={{ height: `${resultados.h20 * 2}px`, minHeight: '10px' }}>
              Sub-base
            </div>
            <div className="base" style={{ height: `${resultados.B * 2}px`, minHeight: '100px' }}>
              Base
            </div>
            <div className="revestimento" style={{ height: `${resultados.R * 2}px`, minHeight: '100px' }}>
              Revestimento
            </div>
          </div>
        </Card>
      )}

      {/* Footer Section */}
      <footer>
        <p className="header-description2">Ferramenta desenvolvida por Gabriella Vilaça, sob orientação do Prof. Pedro Eugênio – PPGES / Escola Politécnica da UPE.</p>
      </footer>
    </main>
  );
}