{
  description = "sch-core-python: python bindings for sch-core";

  inputs.mc-rtc-nix.url = "github:mc-rtc/nixpkgs";

  outputs =
    inputs:
    inputs.mc-rtc-nix.lib.mkFlakoboros inputs (
      { lib, ... }:
      {
        pyOverrideAttrs.sch-core-python = {
          src = lib.cleanSource ./.;
        };
      }
    );
}
