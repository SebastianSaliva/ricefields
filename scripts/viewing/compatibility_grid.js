import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const CompatibilityGrid = () => {
  const distributions = ['MINT', 'UBUNTU', 'DEBIAN', 'MANJARO', 'FEDORA', 'ARCH'];
  const environments = ["GNOME", "KDE_PLASMA", "XFCE", "CINNAMON", "MATE", "LXQT", "BUDGIE", "LXDE", "DDE", "PANTHEON"];

  // Compatibility matrix
  // 2 = Default/Official, 1 = Available/Community, 0 = Via Package Manager Only
  const compatibility = {
    'GNOME': [1, 2, 2, 2, 2, 1],
    'KDE_PLASMA': [1, 2, 2, 2, 2, 1],
    'XFCE': [2, 2, 2, 2, 2, 1],
    'CINNAMON': [2, 0, 0, 1, 1, 1],
    'MATE': [2, 2, 1, 1, 2, 1],
    'LXQT': [0, 2, 1, 1, 2, 1],
    'BUDGIE': [0, 1, 0, 0, 0, 1],
    'LXDE': [0, 0, 1, 0, 0, 1],
    'DDE': [0, 0, 0, 0, 0, 1],
    'PANTHEON': [0, 0, 0, 0, 0, 1]
  };

  const getCompatibilityColor = (value) => {
    switch (value) {
      case 2: return 'bg-green-100 dark:bg-green-900';
      case 1: return 'bg-yellow-100 dark:bg-yellow-900';
      case 0: return 'bg-blue-100 dark:bg-blue-900';
      default: return 'bg-gray-100 dark:bg-gray-800';
    }
  };

  const getCompatibilityText = (value) => {
    switch (value) {
      case 2: return 'Default/Official';
      case 1: return 'Community/Available';
      case 0: return 'Package Manager';
      default: return 'N/A';
    }
  };

  return (
    <Card className="w-full max-w-4xl">
      <CardHeader>
        <CardTitle>Desktop Environment Compatibility Matrix</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="p-2 border">DE / Distro</th>
                {distributions.map(dist => (
                  <th key={dist} className="p-2 border">{dist}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {environments.map(env => (
                <tr key={env}>
                  <td className="p-2 border font-medium">{env}</td>
                  {compatibility[env].map((value, index) => (
                    <td
                      key={index}
                      className={`p-2 border text-center ${getCompatibilityColor(value)}`}
                      title={getCompatibilityText(value)}
                    >
                      {value}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="mt-4 text-sm">
          <p className="mb-2">Legend:</p>
          <ul className="list-none space-y-1">
            <li><span className="inline-block w-4 h-4 bg-green-100 dark:bg-green-900 mr-2"></span>2 = Default/Official Support</li>
            <li><span className="inline-block w-4 h-4 bg-yellow-100 dark:bg-yellow-900 mr-2"></span>1 = Community/Available Support</li>
            <li><span className="inline-block w-4 h-4 bg-blue-100 dark:bg-blue-900 mr-2"></span>0 = Available via Package Manager</li>
          </ul>
        </div>
      </CardContent>
    </Card>
  );
};

export default CompatibilityGrid;