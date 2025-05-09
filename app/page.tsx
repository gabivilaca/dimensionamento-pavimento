'use client';
import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';

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
    <main className="p-6 max-w-4xl mx-auto text-center space-y-6">
      <div className="flex justify-center items-center space-x-4">
        <img src="/upe_poli.png" alt="Logo POLI/UPE" className="h-16" />
        <img src="/ppges.png" alt="Logo PPGES" className="h-16" />
      </div>

      <p className="text-sm text-gray-700 max-w-3xl mx-auto">
        Esta ferramenta foi desenvolvida para auxiliar no cálculo das espessuras das camadas de pavimentos flexíveis,
        com base nas diretrizes do DNIT. Insira os parâmetros abaixo para visualizar os resultados e o gráfico das camadas.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-3xl mx-auto text-left">
        {[
          { name: 'N', label: 'Número de solicitações (N)' },
          { name: 'CBRn', label: 'CBR Subleito (CBRn)' },
          { name: 'CBRSB', label: 'CBR Sub-base (CBRSB)' },
          { name: 'KR', label: 'KR (Coef. Revestimento)' },
          { name: 'KB', label: 'KB (Coef. Base)' },
          { name: 'KSB', label: 'KSB (Coef. Sub-base)' },
        ].map(({ name, label }) => (
          <div key={name}>
            <Label htmlFor={name}>{label}</Label>
            <Input id={name} name={name} value={inputs[name]} onChange={handleChange} type="number" />
          </div>
        ))}
      </div>

      <div className="mt-4">
        <img src="/tabela_dnit.png" alt="Tabela do DNIT" className="mx-auto max-w-full" />
      </div>

      <Button onClick={handleSubmit} className="w-full sm:w-auto mt-4">Calcular Espessuras</Button>

      {resultados && (
        <div className="space-y-4">
          <h3 className="text-lg font-medium mt-6">Resultados:</h3>
          <ul className="text-left inline-block">
            <li><strong>Revestimento (R):</strong> {resultados.R} cm</li>
            <li><strong>Base (B):</strong> {resultados.B.toFixed(2)} cm</li>
            <li><strong>Sub-base (h20):</strong> {resultados.h20.toFixed(2)} cm</li>
          </ul>

          <div className="h-60 w-48 mx-auto relative flex flex-col-reverse items-stretch border">
            <div className="bg-gray-500 text-black text-center text-xs" style={{ height: `${resultados.h20 * 2}px`, minHeight: '10px' }}>
              Sub-base
            </div>
            <div className="bg-gray-400 text-black text-center text-xs" style={{ height: `${resultados.B * 2}px` , minHeight: '100px'}}>
              Base
            </div>
            <div className="bg-gray-300 text-black text-center text-xs" style={{ height: `${resultados.R * 2}px`, minHeight: '100px' }}>
              Revestimento
            </div>
          </div>
        </div>
      )}

      <footer className="text-center text-xs text-gray-600 mt-10 mb-4">
        Ferramenta desenvolvida por Gabriella Vilaça, sob orientação do Prof. Pedro Eugênio – PPGES / Escola Politécnica da UPE.
      </footer>
    </main>
  );
}
