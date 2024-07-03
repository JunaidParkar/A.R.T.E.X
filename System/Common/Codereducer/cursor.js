"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : String(i); }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
var customCursor = /*#__PURE__*/function () {
  function customCursor(cursor) {
    var _this = this;
    var custom = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : false;
    var mediaSize = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 520;
    _classCallCheck(this, customCursor);
    this.cursor = cursor;
    this.custom = custom;
    this.magnetElement = [];
    this.isMagnetActive = false;
    this.mediaSize = mediaSize;
    this.toPerform = window.innerWidth < this.mediaSize ? false : true;
    window.addEventListener("resize", function () {
      return _this.setPerformance();
    });
  }
  _createClass(customCursor, [{
    key: "setPerformance",
    value: function setPerformance() {
      if (window.innerWidth < this.mediaSize) {
        if (this.cursor) {
          this.cursor.style.display = "none";
        }
        this.toPerform = false;
      } else {
        this.toPerform = true;
      }
    }
  }, {
    key: "lerp",
    value: function lerp(x, y, a) {
      return x * (1 - a) + y * a;
    }
  }, {
    key: "createCursor",
    value: function createCursor() {
      if (this.cursor) {
        this.cursor.style.setProperty("all", "unset");
        this.cursor.style.zIndex = 999999999999;
        this.cursor.style.background = "white";
        this.cursor.style.height = "20px";
        this.cursor.style.width = "20px";
        this.cursor.style.borderRadius = "50%";
        this.cursor.style.mixBlendMode = "difference";
        this.cursor.style.position = "fixed";
        this.cursor.style.pointerEvents = "none";
        this.cursor.style.scale = 1;
      }
    }
  }, {
    key: "moveCursor",
    value: function moveCursor(e) {
      if (this.cursor) {
        gsap.to(this.cursor, {
          left: "".concat(e.clientX, "px"),
          top: "".concat(e.clientY, "px"),
          duration: 1,
          ease: Power2.easeOut
        });
        this.cursor.style.left = "".concat(e.clientX, "px");
        this.cursor.style.top = "".concat(e.clientY, "px");
      }
    }
  }, {
    key: "magneticEffect",
    value: function magneticEffect(e) {
      var _this2 = this;
      var _iterator = _createForOfIteratorHelper(this.magnetElement),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var refs = _step.value;
          var _g = refs.getBoundingClientRect();
          var toMagnetize = e.clientX >= _g.left && e.clientX <= _g.right && e.clientY >= _g.top && e.clientY <= _g.bottom;
          if (toMagnetize) {
            this.isMagnetActive = refs;
            break;
          }
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
      if (this.isMagnetActive) {
        var g = this.isMagnetActive.getBoundingClientRect();
        var x = gsap.utils.mapRange(0, g.width, 0, 1, e.clientX - g.left);
        var y = gsap.utils.mapRange(0, g.height, 0, 1, e.clientY - g.top);
        gsap.to(this.isMagnetActive, {
          x: this.lerp(-50, 50, x),
          y: this.lerp(-50, 50, y),
          duration: 1,
          ease: Power2.easeOut
        });
        gsap.to(this.cursor, {
          scale: 4,
          duration: 1,
          ease: Power2.easeOut
        });
        this.isMagnetActive = null;
      }
      this.magnetElement.forEach(function (refs) {
        gsap.to(refs, {
          x: 0,
          y: 0,
          duration: 1,
          ease: Power2.easeOut
        });
        gsap.to(_this2.cursor, {
          scale: 1,
          duration: 1,
          ease: Power2.easeOut
        });
      });
    }
  }, {
    key: "makeMagnet",
    value: function makeMagnet(refArray) {
      var _this3 = this;
      if (this.toPerform) {
        if (refArray.length > 0) {
          refArray.forEach(function (refs) {
            if (refs) {
              _this3.magnetElement.includes(refs) ? "" : _this3.magnetElement.push(refs);
            }
          });
          document.addEventListener("mousemove", function (e) {
            return _this3.magneticEffect(e);
          });
        } else {
          console.warn("No Element passed for magnetic effect");
        }
      } else {
        console.warn("Custom cursor not found on this page");
      }
    }
  }, {
    key: "getCursor",
    value: function getCursor() {
      var _this4 = this;
      if (this.cursor && this.toPerform) {
        if (!this.custom) {
          this.createCursor();
        }
        this.cursor ? this.cursor.style.opacity = 0 : "";
        this.cursor ? this.cursor.classList.add("bui3o87r3r78ry3") : "";
        document.body.style.cursor = "none";
        document.addEventListener("mouseenter", function () {
          return _this4.cursor ? _this4.cursor.style.opacity = 1 : "";
        });
        document.addEventListener("mousemove", function (e) {
          _this4.moveCursor(e);
        });
        document.addEventListener("mouseleave", function () {
          return _this4.cursor ? _this4.cursor.style.opacity = 0 : "";
        });
      } else {
        document.body.style.cursor = "default";
        if (this.cursor) {
          this.cursor.style.display = "none";
        }
      }
    }
  }, {
    key: "revert",
    value: function revert() {
      var _this5 = this;
      document.body.style.cursor = "auto";
      document.removeEventListener("mouseenter", function () {
        return _this5.cursor ? _this5.cursor.style.opacity = 1 : "";
      });
      document.removeEventListener("mousemove", function (e) {
        _this5.moveCursor(e);
      });
      document.removeEventListener("mouseleave", function () {
        return _this5.cursor ? _this5.cursor.style.opacity = 0 : "";
      });
      this.magnetElement = [];
      document.removeEventListener("mousemove", function (e) {
        return _this5.magneticEffect(e);
      });
      this.isMagnetActive = null;
      window.removeEventListener("resize", function () {
        return _this5.setPerformance();
      });
    }
  }]);
  return customCursor;
}();