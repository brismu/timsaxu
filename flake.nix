{
  description = "Prototype distributed Lojban dictionary";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs { inherit system; };
      gismu = pkgs.fetchurl {
        url = "https://www.lojban.org/publications/wordlists/gismu.txt";
        sha256 = "sha256-8vxM/08mWtAnF9VnM7Rif/p4xhbbeNyqRMqraU4d1bc=";
      };
      cmavo = pkgs.fetchurl {
        url = "https://www.lojban.org/publications/wordlists/cmavo.txt";
        sha256 = "sha256-VEQU1h8/813Sz05PefPIa/m7BWjrNAP1cogFfhZ5ZAI=";
      };
      rafsi = pkgs.fetchurl {
        url = "https://www.lojban.org/publications/wordlists/rafsi.txt";
        sha256 = "sha256-MbkKhVHLPLn00MaHOGevGQbpIQw5i/SfIOXCGqAtDSQ=";
      };
      baseline = pkgs.stdenv.mkDerivation {
        name = "baseline.json";
        buildInputs = [ pkgs.python3 ];
        buildCommand = ''
          python3 ${./baseline-convert.py} ${gismu} ${cmavo} ${rafsi}
          mkdir -p $out
          mv baseline.json $out/
        '';
      };
    in {
      packages.default = baseline;
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          python3
        ];
      };
    });
}
