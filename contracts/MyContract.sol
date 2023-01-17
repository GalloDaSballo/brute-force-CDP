// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;


import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MyContract {
  function do_theTHING(IERC20 t) external {
    IERC20(t).transferFrom(address, address(2), 3);
  }
}