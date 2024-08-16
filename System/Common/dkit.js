"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : String(i); }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
var Dkit = /*#__PURE__*/function () {
  function Dkit() {
    _classCallCheck(this, Dkit);
    this.element = null;
  }
  _createClass(Dkit, [{
    key: "id",
    value: function id(_id) {
      this.element = document.getElementById(_id);
      return this;
    }
  }, {
    key: "class",
    value: function _class(className) {
      if (this.element) {
        this.element = this.element.getElementsByClassName(className);
      } else {
        this.element = document.getElementsByClassName(className);
      }
      return this;
    }
  }, {
    key: "from",
    value: function from(element) {
      this.element = element;
      return this;
    }
  }, {
    key: "tag",
    value: function tag(tagName) {
      if (this.element) {
        this.element = this.element.getElementsByTagName(tagName);
      } else {
        this.element = document.getElementsByTagName(tagName);
      }
      return this;
    }
  }, {
    key: "query",
    value: function query(selector) {
      if (this.element) {
        this.element = this.element.querySelector(selector);
      } else {
        this.element = document.querySelector(selector);
      }
      return this;
    }
  }, {
    key: "create",
    value: function create(tag) {
      if (tag) {
        this.element = document.createElement(tag);
      }
      return this;
    }
  }, {
    key: "get",
    value: function get() {
      var data = this.element;
      this.element = null;
      return data;
    }
  }], [{
    key: "init",
    value: function init() {
      return new Dkit();
    }
  }]);
  return Dkit;
}();